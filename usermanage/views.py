# -*- coding:utf8 -*-
from django.shortcuts import render, redirect
from models import User


def register(request):
    print ('过来了')
    if request.method == 'GET':
        # 显示用户注册页面
        return render(request, 'register.html')
    else:
        # 1.接收用户的注册信息
        username = request.POST.get('uname')
        password = request.POST.get('upwd')
        twopwd = request.POST.get('upwdtwo')
        phone = request.POST.get('uphone')
        print username
        users = User.objects.get_one_user(username, None)
        # 3.判断返回值返回json数据
        if users is None:
            print ('没有注册')
            User.objects.add_one_user(name=username, password=password, phone=phone)
        else:
            print ('已经注册')
            context = {'result': '已注册'}
            return render(request, 'register.html', context)

        # 4.跳转到登录页面
        return redirect('/login/')


def login(request):
    return render(request, 'login.html')


def login_handle(request):
    name = request.POST.get('uname')
    users = User.objects.get_one_user(name, None)  # 判断用户是否存在
    # 3.判断返回值返回json数据
    if users is None:
        print ('没有注册')
        return render(request, 'register.html')  # 不存在去注册
    else:
        print ('已经注册')
        name = request.session.get('uname')  # 已经存在查看是否登录过
        if (name):
            return redirect('/index/')    # 没登录过存储一下
        else:
            request.session['uname'] = request.POST['uname']
            return redirect('/index/')


"""
redis存储
 # try:
    #     r = redis.StrictRedis(host='localhost', port=6379)
    # except Exception, e:
    #     print e.message

    # r.delete('name')
    # r.set('name',request.session['uname'])
    #
    # name = r.get('name')
    # print ('redis'+name)
    # print request.session['uname']
"""


def logout(request):
    # request.session['uname'] = None
    # del request.session['uname']
    # request.session.clear()
    request.session.flush()
    return redirect('/index/')


def change_pw(request):
    if request.method == 'GET':
        # 显示用户注册页面
        return render(request, 'change_pw.html')
    else:
        # 1.接收用户的注册信息
        username = request.POST.get('uname')
        password = request.POST.get('upwd')
        phone = request.POST.get('uphone')

        print (username, password, phone)
        # 2.将用户的注册信息添加进数据库
        # Passport.objects.add_one_passport(username=username, password=password, email=email)
        # 注册成功后用celery异步发送邮件给用户
        # 3.给注册用户的邮箱发邮件 smtp
        # msg = '<h1>欢迎您成为天天生鲜的注册会员</h1>请记好您的注册信息<br/>用户名：'+username + '<br/>密码：'+password
        # send_mail('欢迎信息', '', settings.EMAIL_FROM, [email,], html_message=msg)
        # time.sleep(5)
        # register_success_send_mail.delay(username=username, password=password, email=email)
        # 4.跳转到登录页面
        return redirect('/login/')

