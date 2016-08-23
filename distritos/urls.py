# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.DistritoCreateView.as_view(), name='create'),
  	url(r'^list/$', views.DistritoListView.as_view(), name='list'),
  	url(r'^detail/(?P<pk>\d+)/$', views.DistritoDetailView.as_view(), name='detail'),
  	url(r'^update/(?P<pk>\d+)/$', views.DistritoUpdateView.as_view(), name='update'),
  	url(r'^delete/(?P<pk>\d+)/$', views.DistritoDeleteView.as_view(), name='delete'),
]