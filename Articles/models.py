from django.db import models
from datetime import datetime

from mdeditor.fields import MDTextField

from User.models import User


class Classify(models.Model):
    name = models.CharField(max_length=30, verbose_name='文章类别')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Classify'
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name


class Articles(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=100, verbose_name='文章简介', blank=True)
    content = MDTextField()
    comment_num = models.IntegerField(verbose_name='评论数', default=0)
    click_num = models.IntegerField(verbose_name='阅览数', default=0)
    love_num = models.IntegerField(verbose_name='点赞数', default=0)
    add_time = models.DateTimeField(default=datetime.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='文章作者')
    classify = models.ForeignKey(Classify, on_delete=models.CASCADE, verbose_name='文章类别')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Articles'
        ordering = ['-add_time']
        verbose_name = '文字表'
        verbose_name_plural = verbose_name


class Comments(models.Model):
    comment_person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='评论人')
    comment_img = models.ImageField(upload_to='comment_img/%Y/%m/%d/', verbose_name='评论图片', blank=True, null=True)
    comment_content = models.TextField(verbose_name='评论内容',blank=True,null=True)
    comment_time = models.DateTimeField(default=datetime.now, verbose_name='评论时间')
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, verbose_name='评论的文章')

    def __str__(self):
        return self.comment_person

    class Meta:
        db_table = 'Comments'
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name
