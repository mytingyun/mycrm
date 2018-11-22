from hosts import models
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError

class BootStarpModelForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(BootStarpModelForm,self).__init__(*args,**kwargs)
        for k,v in self.fields.items():
            v.widget.attrs['class']='form-control'
            v.widget.attrs['placeholder']=k



class HostModelForm(BootStarpModelForm):
    class Meta:
        model = models.HostManage
        fields = "__all__"
        # widgets = {
        #     'hostname': forms.TextInput(attrs={'class':'form-control','placeholder':'主机名称'}),
        #     'servername':forms.TextInput(attrs={'class':'form-control','placeholder':'功能服务'})
        # }
        # error_messages = {
        #     'hostname':{
        #         'required':'主机名称不能为空'
        #     },
        #     'servername':{
        #         'required':'功能服务不能为空'
        #     }
        # }




class UserModelForm(BootStarpModelForm):
    confirm_pwd = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'确认密码'})
    )

    class Meta:
        model = models.UserList
        fields = ['username','password','confirm_pwd','manhost']
        # widgets = {
        #     'username': forms.TextInput(attrs={'class':'form-control','placeholder':'用户名'}),
        #     'password': forms.PasswordInput(attrs={'class':'form-control','placeholder':'密码'}),
        #     'manhost': forms.Select(attrs={'class':'form-control','placeholder':'管理的主机'}),
        # }

    #勾子函数
    def clean_confirm_pwd(self):
        old = self.cleaned_data['password']
        confirm = self.cleaned_data['confirm_pwd']
        if old != confirm:
            raise ValidationError('两次密码输入不一致')
        return confirm