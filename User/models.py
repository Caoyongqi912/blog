from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    add_time = models.DateTimeField(default=datetime.now, verbose_name='注册时间')
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d/', default='default.png',
                               verbose_name='头像', blank=True, null=True)
    email = models.EmailField(verbose_name='邮箱', unique=True)
    oauth = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'User'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


# 用户登录类型
type = (
    ('1', 'github'),
    ('2', 'qq'),
    ('3', 'weibo')
)


class OAuth_ex(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    openid = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=20, choices=type)


