from django.shortcuts import render,HttpResponse,redirect
from hosts import models
from hosts.form.host_form import HostModelForm,UserModelForm

def userlist(request):
    user_queryset = models.UserList.objects.all()
    return render(request,'userlist.html',{'user_queryset':user_queryset})


def useredit(request,nid):
    pass

def userdel(request,nid):
    pass