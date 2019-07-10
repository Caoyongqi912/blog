from django.db import models

from Product.models import Product
from User.models import User


class AppCase(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='产品',null=True)
    app_case_name = models.CharField(max_length=200,verbose_name='用例名称')
    app_case_result = models.BooleanField('测试结果')
    app_tester = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='测试人')
    create_time = models.DateTimeField(auto_now=True,verbose_name='创建时间')

    def __str__(self):
        return self.app_case_name

    class Meta:
        db_table = 'APP_Case'
        verbose_name =  'app 测试用例'
        verbose_name_plural = verbose_name



class  AppCaseStep(models.Model):
    appcase = models.ForeignKey(AppCase,on_delete=models.CASCADE,verbose_name='测试用例')
    app_test_step = models.CharField(max_length=200,verbose_name='测试步骤')
    app_sbj_name = models.CharField(max_length=200,verbose_name='测试对象名称描述')
    app_find_method = models.CharField(max_length=200,verbose_name='定位方式')
    app_element = models.CharField(max_length=200,verbose_name='控件元素')
    app_opt_method = models.CharField(max_length=200,verbose_name='操作方法')
    app_test_data = models.CharField(max_length=200,null=True,verbose_name='测试数据')
    app_assert_data = models.CharField(max_length=200,verbose_name='验证数据')
    app_res = models.BooleanField(verbose_name='测试结果')
    create_time = models.DateTimeField(auto_now=True,verbose_name='添加时间')

    def __str__(self):
        return self.app_test_step

    class Meta:
        db_table = 'AppCaseStep'
        verbose_name = 'app 案例测试步骤'
        verbose_name_plural = verbose_name



