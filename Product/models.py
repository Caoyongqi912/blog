from django.db import models

# Create your models here.
from User.models import User


class Product(models.Model):
    product_name = models.CharField(max_length=64, verbose_name='产品名称')
    product_desc = models.CharField(max_length=200, verbose_name='产品描述')
    producter = models.ForeignKey(User, verbose_name='产品负责人', on_delete=models.CASCADE,null=True)
    create_time = models.DateTimeField(auto_now=True, verbose_name='增加时间')

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'Product'
        verbose_name = '产品管理'
        verbose_name_plural = verbose_name







