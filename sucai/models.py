# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# 平台
class deck_type(models.Model):
    class Meta:
        verbose_name = '平台'
        verbose_name_plural = '平台'
    pingtai_name = models.CharField(max_length=20, verbose_name='平台名称')

    def __str__(self):
        return "%s" % self.pingtai_name

    def toDict(self):
        return {'name': self.pingtai_name}


# 领域
class field_type(models.Model):
    class Meta:
        verbose_name = '领域'
        verbose_name_plural = '领域'
    deck_type = models.ForeignKey('deck_type', verbose_name='平台')
    lingyu_name = models.CharField(max_length=20, verbose_name='领域名称')

    def __str__(self):
        return "%s" % self.lingyu_name

    def toDict(self):
        return {'name': self.lingyu_name}


# 内容
class message(models.Model):
    class Meta:
        verbose_name = '消息'
        verbose_name_plural = '消息'
    deck_type = models.ForeignKey('deck_type', verbose_name='平台', null=True, blank=True)
    field_type = models.ForeignKey('field_type', verbose_name='领域', null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name='标题')
    message_type = models.IntegerField(default=0, verbose_name='消息类型')
    pinglun_count = models.IntegerField(default=0, verbose_name="评论量")
    yuedu_count = models.IntegerField(default=0, verbose_name="阅读量")
    time = models.CharField(max_length=100, verbose_name="消息时间")
    author = models.CharField(max_length=100, verbose_name="作者", null=True)
    author_img = models.CharField(max_length=300, verbose_name="作者头像链接", null=True, blank=True)
    message_content = models.CharField(max_length=8000, verbose_name="消息内容", null=True, blank=True)
    message_url = models.CharField(max_length=200, verbose_name="文章链接");

    def __str__(self):
        return "%s" % self.title

    def toDict(self):
        return {'title': self.title,
                'message_type': self.message_type, 'pinglun_count': self.pinglun_count,
                'yuedu_count': self.yuedu_count, 'time': self.time, 'message_content': self.message_content, 'message_url':self.message_url}


# 消息图片
class message_img(models.Model):
    class Meta:
        verbose_name = '消息图片'
        verbose_name_plural = '消息图片'
    message = models.ForeignKey('message', verbose_name='消息')
    img_title = models.CharField(max_length=200, verbose_name='图片标题', null=True)
    services_img = models.ImageField(upload_to='img', verbose_name='消息图片')  # 消息图片
    services_img_two = models.ImageField(upload_to='img', verbose_name='消息图片', blank=True)  # 消息图片
    services_img_three = models.ImageField(upload_to='img', verbose_name='消息图片', blank=True)  # 消息图片

    def __str__(self):
        return "%s" % self.img_title

    def toDict(self):
        return {'img_url': self.services_img.url, 'img_url_two': self.services_img_two.url,
                'img_url_three': self.services_img_three.url}
