from django.shortcuts import render,HttpResponse,redirect
from hosts import models
from django.urls import reverse
from hosts.form.host_form import HostModelForm
from hostmanage import settings
from hostmanage.settings import RBAC_SESSION_PERMISSION_KEY

def init_permission(user_object,request):
    """
    权限信息初始化，将权限信息放入session
    :return:
    """
    # 用户正确
    # 1. 获取用户拥有的权限信息
    # 1.1 获取用户拥有的所有角色对象
    # user_object.roles.all()
    # 1.2 django连表 + 去重 + 空值的判断
    #permissions__title__isnull=False 让权限表中的title不等于None
    permission_list = user_object.roles.filter(permissions__title__isnull=False).values('permissions__title',
                                                                                        'permissions__url',
                                                                                        'permissions__name',
                                                                                        'permissions__is_menu',
                                                                                        ).distinct()
    """
    permission_list = [
        {'permissions__title': '部门列表', 'permissions__url': '/depart/list/', 'permissions__name': 'depart_list', 'permissions__is_menu': True},
        {'permissions__title': '添加部门', 'permissions__url': '/depart/add/', 'permissions__name': 'depart_add', 'permissions__is_menu': False},
        {'permissions__title': '编辑部门', 'permissions__url': '/depart/edit/(\\d+)/', 'permissions__name': 'depart_edit', 'permissions__is_menu': False},
        {'permissions__title': '删除部门', 'permissions__url': '/depart/del/(\\d+)/', 'permissions__name': 'depart_del', 'permissions__is_menu': False},
        {'permissions__title': '用户列表', 'permissions__url': '/user/list/', 'permissions__name': 'user_list', 'permissions__is_menu': True},
        {'permissions__title': '添加用户', 'permissions__url': '/user/add/', 'permissions__name': 'user_add', 'permissions__is_menu': False},
        {'permissions__title': '编辑用户', 'permissions__url': '/user/edit/(\\d+)/', 'permissions__name': 'user_edit', 'permissions__is_menu': False},
        {'permissions__title': '删除用户', 'permissions__url': '/user/del/(\\d+)/', 'permissions__name': 'user_del', 'permissions__is_menu': False},
    ]

    """
    # 2. 对权限信息进行结构处理
    permission_dict = {}
    menu_list = []
    #循环权限列表
    for item in permission_list:
        #如果列表中权限菜单为true
        if item['permissions__is_menu']:
            #收集此项的title,url,name,
            menu_list.append({
                'title': item['permissions__title'],
                'url': item['permissions__url'],
                'name': item['permissions__name'],
            })
        permission_dict[item['permissions__name']] = {'url': item['permissions__url']}
    # for item in permission_list:
    #     permission_dict[item['permissions__name']] = {'url': item['permissions__url']}
    """
    {
        depart_list:{'url':'/depart/list/' },

    }
    """
    # 3. 放入session
    print(permission_dict)
    request.session[settings.RBAC_SESSION_PERMISSION_KEY] = permission_dict
    request.session[settings.RBAC_SESSION_MENU_KEY] = menu_list
    request.session.set_expiry(0)







def login(request):
    if request.method == 'GET':
        return render(request,'login.html')

    username = request.POST.get('username')
    passwd = request.POST.get('password')
    user_object = models.UserList.objects.filter(username=username,password=passwd).first()
    if not user_object:
        return render(request,'login.html',{'error':'用户名或密码错误'})

    init_permission(user_object, request)
    print(user_object.username)
    return redirect(reverse('index'))



def logout(request):
    request.session.delete()
    return redirect('/hosts/login/')


def index(request):
    return render(request,'index.html')


def lists(request):
    host_queryset = models.HostManage.objects.all()
    return render(request,'hostlist.html',{'host_queryset':host_queryset})

def hostadd(request):
    """
    添加主机
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = HostModelForm()
        return render(request,'hostdefault.html',{'form':form})
    form = HostModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/hosts/list/')
    return render(request,'hostdefault.html',{'form':form})

def hostedit(request,nid):
    """
    编辑主机
    :param request:
    :return:
    """
    obj = models.HostManage.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = HostModelForm(instance=obj)
        return render(request,'hostdefault.html',{'form':form})
    form = HostModelForm(data=request.POST,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/hosts/list/')
    return render(request, 'hostdefault.html', {'form': form})


def hostsdel(request,nid):
    """
    删除主机
    :param request:
    :param nid:
    :return:
    """
    origin = reverse('hostlist')
    if request.method == 'GET':
        return render(request, 'delete.html', {'cancel':origin})
    models.HostManage.objects.filter(id=nid).delete()
    return redirect(origin)

