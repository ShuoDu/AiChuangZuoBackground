from django.shortcuts import render


def movie_list(request):
    return render(request, 'moving.html')
