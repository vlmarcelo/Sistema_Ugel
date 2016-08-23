# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.ClaseEntidadCreateView.as_view(), name='create'),
  	url(r'^list/$', views.ClaseEntidadListView.as_view(), name='list'),
  	url(r'^update/(?P<pk>\d+)/$', views.ClaseEntidadUpdateView.as_view(), name='update'),
  	url(r'^delete/(?P<pk>\d+)/$', views.ClaseEntidadDeleteView.as_view(), name='delete'),
]