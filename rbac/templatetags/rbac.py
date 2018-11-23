import re
from django.template import Library
from django.conf import settings

register = Library()

# 用于在为模板自定义函数，调用方式： {% func 1 2 3 4 %}
@register.simple_tag
def func(a1,a2,a3,a4):
    return a1 + "666"

# 用于在为模板自定义函数，调用方式： {{ '张三'|foo:"dsb" }} + 可以在 if后面做条件
@register.filter
def foo(a1,a2):
    return '999'

# 用于返回一个代码块
@register.inclusion_tag('rbac/menu.html')
def get_menu(request):
    menu_list = request.session.get(settings.RBAC_SESSION_MENU_KEY)
    """
    [
        {
            'title':'x1',
            'url':'/xxx/',
            'name':x1,
        },
        {
            'title':'x1',
            'url':'/xxx/',
            'name':x1,
            'class':'active'
        }
    ]
    """
    for item in menu_list:
        url = '^%s$' % item['url']
        if re.match(url,request.path_info):
            item['class'] = 'active'
    return {
        'menu_list': menu_list
    }

@register.filter
def has_permission(request,name):
    """
    判断用户是否有该name权限
    :param request:
    :param name:
    :return:
    """
    permission_dict = request.session.get(settings.RBAC_SESSION_PERMISSION_KEY)
    if name in permission_dict:
        return True
