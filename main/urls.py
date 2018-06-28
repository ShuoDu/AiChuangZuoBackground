from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/(\d*)/$', views.index),
    url(r'^$', views.main),
    url(r'^login/$', views.login),
    url(r'^testjs/$', views.testJs),
    url(r'^switch/$', views.switchMessage),
]
