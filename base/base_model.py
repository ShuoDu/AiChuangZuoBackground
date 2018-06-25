# -*- coding:utf8 -*-
from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True  # 说明是一个抽象模型类