"""hostmanage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from hosts.views import hostm
from hosts.views import users

urlpatterns = [
    url(r'^hosts/index/$', hostm.index),
    url(r'^login/$', hostm.login),
    url(r'^logout/$', hostm.logout),
    url(r'^hosts/list/$', hostm.lists,name='hostlist'),
    url(r'^hosts/add/$', hostm.hostadd,name='hostadd'),
    url(r'^hosts/edit/(\d+)/$', hostm.hostedit,name='hostedit'),
    url(r'^hosts/del/(\d+)/$', hostm.hostsdel,name='hostdel'),
    url(r'^user/list/$', users.userlist,name='userlist'),
    url(r'^user/edit/(\d+)/$', users.useredit, name='useredit'),
    url(r'^user/del/(\d+)/$', users.userdel, name='userdel'),

]
