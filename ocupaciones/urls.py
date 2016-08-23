# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.OcupacionCreateView.as_view(), name='create'),
  	url(r'^list/$', views.OcupacionListView.as_view(), name='list'),
  	url(r'^update/(?P<pk>\d+)/$', views.OcupacionUpdateView.as_view(), name='update'),
  	url(r'^delete/(?P<pk>\d+)/$', views.OcupacionDeleteView.as_view(), name='delete'),
]