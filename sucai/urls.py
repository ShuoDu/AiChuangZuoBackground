from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^deck_list/$', views.deck_list),
    url(r'^field_list/$', views.field_list),
    url(r'^list/$', views.list),
    url(r'^all/$', views.all),
]
