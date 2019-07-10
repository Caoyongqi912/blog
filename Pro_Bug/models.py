from django.db import models

# Create your models here.
from Product.models import Product
from User.models import User

STATUS = (('激活','激活'),('已解决','已解决'),('已关闭','已关闭'))
LEVEL = (('1','1'),('2','2'),('3','3'))
class Bug(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    bug_name = models.CharField(max_length=64,verbose_name='bug名称')
    bug_detail = models.CharField(max_length=200,verbose_name='bug详情')
    bug_status = models.CharField(max_length=200,verbose_name='bug状态',null=True,default='激活',choices=STATUS)
    bug_level = models.CharField(max_length=200,verbose_name='bug等级',default='3',choices=LEVEL)
    bug_creater = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='bug创建人')
    bug_assign = models.CharField(max_length=200,verbose_name='分配给')
    create_time = models.DateTimeField(auto_now=True,verbose_name='创建时间')

    def __str__(self):
        return self.bug_name

    class Meta:
        db_table = 'Bug'
        verbose_name = 'bug管理'
        verbose_name_plural = verbose_name
