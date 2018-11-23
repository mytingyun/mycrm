from django.db import models



class Permission(models.Model):
    """
    权限表
    """
    title = models.CharField(verbose_name='名称',max_length=32)
    name = models.CharField(verbose_name='URL别名',max_length=32,unique=True)
    url = models.CharField(verbose_name='URL',max_length=32)
    is_menu = models.BooleanField(verbose_name='是否是菜单',default=False)

    def __str__(self):
        return self.title

class Role(models.Model):
    """
    角色表
    """
    title = models.CharField(verbose_name='名称',max_length=32)
    permissions = models.ManyToManyField(verbose_name='拥有的权限',to='Permission',blank=True)

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """
    用户表
    """
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    roles = models.ManyToManyField(verbose_name='拥有的角色',to=Role)

    class Meta:
        abstract = True
