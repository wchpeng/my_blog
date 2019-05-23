# -*- coding:utf8 -*-
from django.db import models
from django.conf import settings
from django.utils import timezone

from utils.markdown_util import md2html


class BlogTag(models.Model):
    name = models.CharField(max_length=16, verbose_name="标签名称")
    creater_id = models.IntegerField(verbose_name="创建人", default=-1)

    class Meta:
        ordering = ("-id",)
        verbose_name = "标签"
        verbose_name_plural = "标签"

    def __str__(self):
        return self.name


class BlogCategory(models.Model):
    name = models.CharField(max_length=16, verbose_name="类别名称")
    creater_id = models.IntegerField(verbose_name="创建人", default=-1)

    class Meta:
        ordering = ("-id",)
        verbose_name = "分类"
        verbose_name_plural = "分类"

    def __str__(self):
        return self.name


class Blog(models.Model):
    creater = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="作者")
    title = models.CharField(max_length=32, verbose_name="标题", default="")
    is_md = models.BooleanField(verbose_name='markdown')
    text = models.TextField(verbose_name="文章内容")
    text_html = models.TextField(verbose_name="文章内容（html）")
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, verbose_name="种类")
    tags = models.ManyToManyField(BlogTag, verbose_name="标签")
    expire_to = models.DateTimeField(verbose_name="过期时间", default=timezone.now)
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        ordering = ("-id",)
        verbose_name = "博客"
        verbose_name_plural = "博客"

    def __str__(self):
        return self.creater.username + "   " + self.title
