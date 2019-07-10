from django.db import models


#
class QuanJi(models.Model):
    m_name = models.CharField(max_length=100, verbose_name='电影名')
    m_img = models.CharField(max_length=300, verbose_name='电影图')
    m_url = models.CharField(max_length=400, verbose_name='下载地址')
    m_content = models.CharField(max_length=1000, verbose_name='简介')

    def __str__(self):
        return self.m_name

    class Mete:
        db_table = 'spider'


class Cat_eye(models.Model):
    movieName = models.CharField(max_length=50, verbose_name='電影名')
    releaseInfo = models.CharField(max_length=10, verbose_name='上映天数')
    sumBoxInfo = models.CharField(max_length=50, verbose_name='綜合票房')
    boxInfo = models.CharField(max_length=50, verbose_name='票房占比')
    boxRate = models.CharField(max_length=50, verbose_name='排片場次')
    avgShowView = models.CharField(max_length=50, verbose_name='人均场次')
    avgSeatView = models.CharField(max_length=50, verbose_name='上座率')

    def __str__(self):
        return self.movieName

    class Meta:
        db_table = 'cat_eyes'
