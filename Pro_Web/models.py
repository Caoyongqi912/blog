from django.db import models

# Create your models here.
from Product.models import Product
from User.models import User


class WebCase(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='产品')

    web_case_name = models.CharField(max_length=200,verbose_name='用例名称')
    web_test_res = models.BooleanField(verbose_name='测试结果')
    web_tester = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='测试人')
    create_time = models.DateTimeField(auto_now=True,verbose_name='创建时间')

    def __str__(self):
        return self.web_case_name

    class Meta:
        db_table = 'WebCase'
        verbose_name = 'WEB 测试用例'
        verbose_name_plural = verbose_name


class WebCaseStep(models.Model):
    web_case = models.ForeignKey(WebCase,on_delete=models.CASCADE,verbose_name='用例名称')
    web_case_name = models.CharField(max_length=200,verbose_name='测试用例标题')
    web_test_step = models.CharField(max_length=200,verbose_name='测试步骤')
    web_sbj_name = models.CharField(max_length=200,verbose_name='测试对象描述')

    web_find_method = models.CharField(max_length=200,verbose_name='定位方式')
    web_element = models.CharField(max_length=200,verbose_name='控件元素')
    web_opt_method = models.CharField(max_length=200,verbose_name='操作方法')

    web_test_data = models.CharField(max_length=200,null=True,verbose_name='测试数据')
    web_assert_data = models.CharField(max_length=200,verbose_name='验证数据')
    web_test_res  = models.BooleanField(verbose_name='测试结果')
    create_time = models.DateTimeField(auto_now=True,verbose_name='创建时间')

    def __str__(self):
        return self.web_case_name

    class Meta:
        db_table = 'WebCaseStep'
        verbose_name = 'Web 用例方法步骤'
        verbose_name_plural = verbose_name
