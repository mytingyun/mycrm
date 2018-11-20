from django.db import models

# Create your models here.



class HostManage(models.Model):
    """
    主机管理
    """
    hostname = models.CharField(verbose_name='主机名',max_length=64)
    servername = models.CharField(verbose_name='服务功能',max_length=32)

    def __str__(self):
        return self.hostname

class UserList(models.Model):
    """
    用户管理
    """
    username = models.CharField(verbose_name='用户名', max_length=64)
    password = models.CharField(verbose_name='密码', max_length=32)
    manhost = models.ForeignKey(verbose_name='管理的主机', to=HostManage)
    def __str__(self):
        return self.username