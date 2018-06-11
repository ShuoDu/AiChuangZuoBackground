# -*- coding:utf8 -*-
from django.shortcuts import render
from sucai import models
import json


# 转换成json形式
def toDicts(objs):
    obj_arr = []
    for o in objs:
        obj_arr.append(o.toDict())
    return obj_arr


def index(request):
    all_deck = models.deck_type.objects.all()  # 获取所有平台类型
    all_type = models.field_type.objects.all()  # 获取所有分类
    all_objs = models.message.objects.all()  # 获取列表

    all_dicts = toDicts(all_objs)
    print all_dicts
    all_json = json.dumps(all_dicts, ensure_ascii=False)

    context = {'message': all_objs, 'type': all_type, 'deck': all_deck}
    # return HttpResponse(all_json)
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')
