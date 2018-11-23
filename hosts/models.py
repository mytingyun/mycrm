from django.db import models
from rbac.models import UserInfo



class HostManage(models.Model):
    """
    主机管理
    """
    hostname = models.CharField(verbose_name='主机名',max_length=64)
    servername = models.CharField(verbose_name='服务功能',max_length=32)

    def __str__(self):
        return self.hostname

class UserList(UserInfo):
    """
    用户管理
    """
    emails = models.EmailField(verbose_name='邮件',max_length=32)
    manhost = models.ForeignKey(verbose_name='管理的主机', to=HostManage)
