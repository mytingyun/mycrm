from hosts import models
from django import forms
from django.forms import ModelForm


class HostModelForm(ModelForm):
    class Meta:
        model = models.HostManage
        fields = "__all__"
        widgets = {
            'hostname': forms.TextInput(attrs={'class':'form-control','placeholder':'主机名称'}),
            'servername':forms.TextInput(attrs={'class':'form-control','placeholder':'功能服务'})
        }
        error_messages = {
            'hostname':{
                'required':'主机名称不能为空'
            },
            'servername':{
                'required':'功能服务不能为空'
            }
        }


class UserModelForm(ModelForm):
    class Meta:
        model = models.UserList
        fields = "__all__"
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'用户名'}),
            'password': forms.TextInput(attrs={'class':'form-control','placeholder':'密码'}),
            'manhost': forms.Select(attrs={'class':'form-control','placeholder':'管理的主机'}),
        }
