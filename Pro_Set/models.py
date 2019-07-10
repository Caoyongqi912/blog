from django.db import models

class Set(models.Model):
    set_name = models.CharField(max_length=64,verbose_name='系统名称')
    set_value = models.CharField(max_length=200,verbose_name='设置值')

    def __str__(self):
        return self.set_name

    class Meta:
        db_table = 'Set'
        verbose_name = '系统设置'
        verbose_name_plural = verbose_name
