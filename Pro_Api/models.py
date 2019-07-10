from django.db import models

# Create your models here.
from Product.models import Product
from User.models import User


class ApiTest(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='产品', null=True)
    api_test_name = models.CharField(max_length=64, null=False, blank=False, verbose_name='流程接口名')
    api_test_desc = models.CharField(max_length=64, null=False, blank=False, verbose_name='描述')
    api_tester = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='执行人')
    api_test_res = models.BooleanField(verbose_name='测试结果')
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    def __str__(self):
        return self.api_test_name

    class Meta:
        db_table = 'ApiTest'
        verbose_name = '用例'
        verbose_name_plural = verbose_name


REQUEST_METHOD = (('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete',
                                                                     'delete'),
                  ('patch', 'patch'))


class ApiTestStep(models.Model):
    api_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='用例名称')
    api_url = models.CharField(max_length=200, null=False, blank=False, verbose_name='接口URL')
    api_step = models.CharField(max_length=100, null=True, verbose_name='测试步骤')
    api_param_val = models.CharField(max_length=800, null=False, blank=False, verbose_name='请求参数与值')
    api_method = models.CharField(max_length=200, null=True, verbose_name='接口方法', default='get',
                                  choices=REQUEST_METHOD)
    api_result = models.CharField(max_length=200, null=False, blank=False, verbose_name='接口预期结果')
    api_response = models.CharField(max_length=5000, null=True, blank=True, verbose_name='响应数据')
    api_status = models.BooleanField(verbose_name='是否通过')
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    api_test = models.ForeignKey(ApiTest, on_delete=models.CASCADE)

    def __str__(self):
        return self.api_name

    class Meta:
        db_table = 'ApiTestStep'
        verbose_name = '用例方法'
        verbose_name_plural = verbose_name




class Apis(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, verbose_name='产品')
    api_name = models.CharField(max_length=100, verbose_name='接口名称')
    api_url = models.CharField(max_length=200, verbose_name='url地址')
    api_par_val = models.CharField(max_length=800, verbose_name='请求参数和值')
    api_method = models.CharField(choices=REQUEST_METHOD, default='get', max_length=200, verbose_name='请求参数')
    api_result = models.CharField(max_length=200, verbose_name='预期结果')
    api_status = models.BooleanField(verbose_name='是否通过')
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    def __str__(self):
        return self.api_name

    class Meta:
        db_table = 'Apis'
        verbose_name = '单一场景接口'
        verbose_name_plural = verbose_name