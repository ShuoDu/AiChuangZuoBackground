from django.shortcuts import render


def tark(request):
    return render(request, 'manage.html')
