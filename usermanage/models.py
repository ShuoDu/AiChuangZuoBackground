# -*- coding:utf8 -*-
from __future__ import unicode_literals
from django.db import models
from base.base_model import BaseModel
from base.base_manager import BaseManager
from util import get_hash


# 用户模型管理器类
class UserManager(BaseManager):
    # 添加一个账户
    def add_one_user(self, name, password, phone):
        # 获取self所在的模型类
        model_class = self.model
        # 创建一个模型对象
        users = model_class()
        users.name = name
        users.password = password
        users.phone = phone
        #  保存到数据库
        users.save()
        return users

    # 第二种添加方法
    def add_one_users1(self, name, password, phone):
        users = self.create_one_object(name=name, password=password, phone=phone)
        return users

    # 根据用户名和密码查询账户信息
    def get_one_user(self, username, password):

        try:
            if password is None:
                print ('只根据用户名查找')
                # 根据用户名查找
                users = self.get(name=username)
            else:
                # 根据用户名密码查找
                users = self.get(name=username, password=password)

        except self.model.DoesNotExist:
            # 用get方法返回单个满足条件的对象，没查到会引发"模型类.DoesNotExist"异常，需要返回一个空值
            # 查询集用 filter all
            users = None

        return users

    #  第二种方法查询单个对象
    def get_one_users1(self, username, password=None):    # 根据用户名密码查询账户信息

        if password is None:
            # 根据用户名查找账户信息
            users = self.get_one_object(name=username)
        else:
            # 根据用户名和密码查询账户信息
            users = self.get_one_object(name=username, password=get_hash(password))
        return users


class User (BaseModel):
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
    name = models.CharField(max_length=20, verbose_name='用户名')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='手机号')
    password = models.CharField(max_length=100, verbose_name='密码')
    message_pw = models.IntegerField(default=0, null=True, blank=True, verbose_name='验证码')
    objects = UserManager()  # 自定义模型管理器对象

    def __str__(self):
        return "%s" % self.name



