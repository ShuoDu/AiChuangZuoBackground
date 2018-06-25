# -*- coding:utf8 -*-
from django.shortcuts import render
from sucai import models
import json
from django.http import HttpResponse


# 转换成json形式
def toDicts(objs):
    obj_arr = []
    for o in objs:
        obj_arr.append(o.toDict())
    return obj_arr
'''
 if request.method == 'POST':
        values = request.POST
        deck_name = values['data']
        deck_id = models.deck_type.objects.get(pingtai_name=deck_name)
        all_objs = models.message.objects.filter(deck_type_id=deck_id)  #筛选
        print all_objs
        # all_objs = models.message.objects.all()  # 获取列表
        all_dicts = toDicts(all_objs)
        all_json = json.dumps(all_dicts, ensure_ascii=False)

        all_deck = models.deck_type.objects.all()  # 获取所有平台类型
        all_type = models.field_type.objects.all()  # 获取所有分类
        context = {'message': all_objs, 'type': all_type, 'deck': all_deck}
        # return HttpResponse(all_json)
        # return render(request, 'index.html', context)
        return HttpResponse(all_json)
'''


def main(request):
        print ('普通请求')
        all_deck = models.deck_type.objects.all()  # 获取所有平台类型
        all_type = models.field_type.objects.all()  # 获取所有分类
        all_objs = models.message.objects.all()  # 获取列表
        all_dicts = toDicts(all_objs)
        print all_dicts
        all_json = json.dumps(all_dicts, ensure_ascii=False)

        # return HttpResponse(all_json)
        uname = request.session.get('uname')
        if uname:
            print ('登录名' + uname)
        context = {'message': all_objs, 'type': all_type, 'deck': all_deck, 'uname': uname}
        return render(request, 'index.html', context)


def switchMessage(request):
    type = request.GET['type']
    deck_id = models.deck_type.objects.get(pingtai_name=type)
    all_objs = models.message.objects.filter(deck_type_id=deck_id)  # 筛选
    all_deck = models.deck_type.objects.all()  # 获取所有平台类型
    all_type = models.field_type.objects.all()  # 获取所有分类
    uname = request.session.get('uname')
    print ('登录名' + uname)
    context = {'message': all_objs, 'type': all_type, 'deck': all_deck, 'uname': uname}
    return render(request, 'index.html', context)


def index(request, page):
    page = int(page)
    start = (page-1)*3
    end = (page*3)
    all_deck = models.deck_type.objects.all()  # 获取所有平台类型
    all_type = models.field_type.objects.all()  # 获取所有分类

    count = models.message.objects.all()[start:end].count()

    all_objs = models.message.objects.all()[start:end]  # 获取列表

    all_dicts = toDicts(all_objs)

    all_json = json.dumps(all_dicts, ensure_ascii=False)

    uname = request.session.get('uname')
    print ('登录名'+uname)

    context = {'message': all_objs, 'count': count, 'type': all_type, 'deck': all_deck, 'uname': uname}
    # return HttpResponse(all_json)
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')


# ajax请求
def testJs (request):
     if request.method == 'POST':
         print request.POST
         all_objs = models.message.objects.all()  # 获取列表
         all_dicts = toDicts(all_objs)
         all_json = json.dumps(all_dicts, ensure_ascii=False)
         return HttpResponse(all_json)
     else:
         return render(request, "testJs.html")


