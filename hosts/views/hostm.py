from django.shortcuts import render,HttpResponse,redirect
from hosts import models
from django.urls import reverse
from hosts.form.host_form import HostModelForm,UserModelForm
from hostmanage.settings import RBAC_SESSION_PERMISSION_KEY

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == "POST":
        username = request.POST.get('username')
        passwd = request.POST.get('password')
        user_object = models.UserList.objects.filter(username=username,password=passwd).first()
        if not user_object:
            return render(request,'login.html',{'error':'用户名或密码错误'})
        request.session[RBAC_SESSION_PERMISSION_KEY] = 'abc123'
        request.session.set_expiry(0)
        return redirect('/hosts/index/')
    return render(request,'login.html')

def logout(request):
    del request.session[RBAC_SESSION_PERMISSION_KEY]
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

