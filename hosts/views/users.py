from django.shortcuts import render,HttpResponse,redirect
from hosts import models
from django.urls import reverse
from hosts.form.host_form import HostModelForm,UserModelForm

def userlist(request):
    """
    用户列表
    :param request:
    :return:
    """
    user_queryset = models.UserList.objects.all()
    return render(request,'userlist.html',{'user_queryset':user_queryset})

def useradd(request):
    """增加用户"""
    if request.method == 'GET':
        form = UserModelForm()
        return render(request,'userdefault.html',{'form':form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request,'userdefault.html',{'form':form})


def useredit(request,nid):
    """
    编辑用户
    :param request:
    :param nid:
    :return:
    """
    obj = models.UserList.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = UserModelForm(instance=obj)
        return render(request,'userdefault.html',{'form':form})
    form = UserModelForm(data=request.POST,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request,'userdefault.html',{'form':form})

def userdel(request,nid):
    """
    删除主机
    :param request:
    :param nid:
    :return:
    """
    cancel = reverse('userlist')
    if request.method == 'GET':
        return render(request,'delete.html',{'cancel':cancel})
    models.UserList.objects.filter(id=nid).delete()
    return redirect(cancel)