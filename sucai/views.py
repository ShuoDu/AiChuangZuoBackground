# -*- coding: utf-8 -*-

from django.http import HttpResponse
import json
import models


# 转换成json形式
def toDicts(objs):
    obj_arr = []
    for o in objs:
        obj_arr.append(o.toDict())
    return obj_arr


# 查询平台类型
def deck_list(request):
    all_type = models.deck_type.objects.all()
    all_dicts = toDicts(all_type)
    all_json = json.dumps(all_dicts, ensure_ascii=False)
    return HttpResponse(all_json)


# 查询平台领域类型
def field_list(request):
    deck = request.GET.get('deck_type')
    print deck
    deck_id = models.deck_type.objects.get(pingtai_name=deck)

    all_objs = models.field_type.objects.filter(deck_type_id=deck_id)  # 获取列表用filter,获取单个值用get
    all_dicts = toDicts(all_objs)
    all_json = json.dumps(all_dicts, ensure_ascii=False)
    return HttpResponse(all_json)


# 筛选消息
def list(request):
    deck = request.GET.get('deck')
    filters = request.GET.get('filters')

    print deck
    print filters

    deck_id = models.deck_type.objects.get(pingtai_name=deck)
    filter_id = models.field_type.objects.get(deck_type_id=deck_id, lingyu_name=filters)

    all_objs = models.message.objects.filter(deck_type_id=deck_id, field_type_id=filter_id)  # 获取列表用filter,获取单个值用get
    all_dicts = toDicts(all_objs)
    all_json = json.dumps(all_dicts, ensure_ascii=False)
    return HttpResponse(all_json)


# 查询所有消息
def all(request):
    all_objs = models.message.objects.all()  # 获取列表
    all_dicts = toDicts(all_objs)
    all_json = json.dumps(all_dicts, ensure_ascii=False)
    return HttpResponse(all_json)
