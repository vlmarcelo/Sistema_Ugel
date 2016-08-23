# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.DepartamentoCreateView.as_view(), name='create'),
  	url(r'^list/$', views.DepartamentoListView.as_view(), name='list'),
  	url(r'^detail/(?P<pk>\d+)/$', views.DepartamentoDetailView.as_view(), name='detail'),
  	url(r'^update/(?P<pk>\d+)/$', views.DepartamentoUpdateView.as_view(), name='update'),
  	url(r'^delete/(?P<pk>\d+)/$', views.DepartamentoDeleteView.as_view(), name='delete'),
]