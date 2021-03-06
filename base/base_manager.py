# -*- coding:utf8 -*-
from django.db import models
import copy


class BaseManager(models.Manager):

    def get_all_valid_fields(self):
        '''
        获取self所在模型类的有效属性的字符串列表
        '''
        # 1.获取self所在的模型类
        model_class = self.model
        # 2.获取model_class模型类的属性元组
        attr_tuple = model_class._meta.get_fields()
        str_attr_list = []
        for attr in attr_tuple:
            # print(attr.name)
            if isinstance(attr, models.ForeignKey):  # _id
                str_attr = '%s_id' % attr.name
            else:
                str_attr = attr.name
            # str_attr_list.append(attr.name)
            str_attr_list.append(str_attr)

        return str_attr_list

    def create_one_object(self, **kwargs):
        '''
        添加一个self所在模型类的对象
        '''
        # 1.获取self所在模型类的有效属性的字符串列表
        valid_fields = self.get_all_valid_fields()
        # 2.拷贝一份kwargs
        kws = copy.copy(kwargs)
        # 3.去除ｋｗargs参数中self.model的无效属性
        for key in kws:
            if key not in valid_fields:
                kwargs.pop(key)

        # 4.获取self所在的模型类
        model_class = self.model
        # 5.创建一个model_class的对象
        obj = model_class(**kwargs)
        # 6.调用obj的save方法将数据保存进数据库
        obj.save()
        # 7.返回这个对象
        return obj

    def get_one_object(self, **filters):
        '''
        根据filters条件查询self.model模型类的对象
        '''
        try:
            obj = self.get(**filters)
        except self.model.DoesNotExist:
            obj = None
        return obj

    def get_object_list(self, filters={}, exclude_filtes={}, order_by=('-pk',)):
        '''
        查询self.model模型类对应的查询集 QuerySet
        '''
        object_list = self.filter(**filters).exclude(**exclude_filtes).order_by(*order_by)
        return object_list























