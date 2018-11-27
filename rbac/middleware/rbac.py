import re
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.urls import reverse
from django.shortcuts import HttpResponse,redirect


class RbacMiddleware(MiddlewareMixin):

    def process_request(self,request):
        """
        权限的校验
        :param request:
        :return:
        """
        # 1. 处理白名单
        for reg in settings.RBAC_VALID_LIST:
            if re.match(reg,request.path_info):
                return None

        # 2. 权限校验
        # 去session中获取当前用户的权限信息
        # 当前请求的URL
        """
        {
            'depart_list': {'url': '/depart/list/'}, 
            'depart_add': {'url': '/depart/add/'}, 
            'depart_edit': {'url': '/depart/edit/(\\d+)/'}, 
            'depart_del': {'url': '/depart/del/(\\d+)/'}, 
            'user_list': {'url': '/user/list/'},
             'user_add': {'url': '/user/add/'}, 
             'user_edit': {'url': '/user/edit/(\\d+)/'}, 
             'user_del': {'url': '/user/del/(\\d+)/'}
        }
        """
        permission_dict = request.session.get(settings.RBAC_SESSION_PERMISSION_KEY)
        if not permission_dict:
            return redirect(reverse('login'))

        for reg in settings.RBAC_NO_PERMISSION_LIST:
            if re.match(reg,request.path_info):
                return None

        for name,url_info in permission_dict.items():
            url = "^%s$" % url_info['url']
            if re.match(url,request.path_info):
                return None
        return redirect(reverse('login'))
