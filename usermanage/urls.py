from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^login_handle/$', views.login_handle, name='login_handle'),
    url(r'^logout/$', views.logout),
    url(r'^change_pw/$', views.change_pw),
]
