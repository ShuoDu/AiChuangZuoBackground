"""aichuangzuo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('work_tark.urls', namespace='main')),
    url(r'^index/', include('main.urls')),
    url(r'^sucai/', include('sucai.urls')),
    url(r'^user/', include('usermanage.urls')),
    url(r'^baowen/', include('baowen.urls')),
    url(r'^talk/', include('talkings.urls')),
    url(r'^movie/', include('movigs.urls')),
    url(r'^tark/', include('work_tark.urls')),
]
