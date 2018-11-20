from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect,render
from hostmanage import settings

waitelist = ['/login/','/hosts/index/']

class HostMiddleware(MiddlewareMixin):
    def process_request(self,request):

        if request.path_info in waitelist:
            return None

        permission = request.session.get(settings.RBAC_SESSION_PERMISSION_KEY)
        if not permission:
            return redirect('/login/')
        return None