# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.ZonaCreateView.as_view(), name='create'),
  	url(r'^list/$', views.ZonaListView.as_view(), name='list'),
  	url(r'^update/(?P<pk>\d+)/$', views.ZonaUpdateView.as_view(), name='update'),
  	url(r'^delete/(?P<pk>\d+)/$', views.ZonaDeleteView.as_view(), name='delete'),
]