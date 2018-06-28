# -*- coding:utf8 -*-
from django.shortcuts import render


def talk_list(request):
    return render(request, 'talking.html')
