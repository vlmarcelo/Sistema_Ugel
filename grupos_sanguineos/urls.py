# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.GrupoSanguineoCreateView.as_view(), name='create'),
  	url(r'^list/$', views.GrupoSanguineoListView.as_view(), name='list'),
  	url(r'^detail/(?P<pk>\d+)/$', views.GrupoSanguineoDetailView.as_view(), name='detail'),
  	url(r'^update/(?P<pk>\d+)/$', views.GrupoSanguineoUpdateView.as_view(), name='update'),
  	url(r'^delete/(?P<pk>\d+)/$', views.GrupoSanguineoDeleteView.as_view(), name='delete'),
]