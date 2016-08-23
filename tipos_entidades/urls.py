# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.TipoEntidadCreateView.as_view(), name='create'),
  	url(r'^list/$', views.TipoEntidadListView.as_view(), name='list'),
  	url(r'^update/(?P<pk>\d+)/$', views.TipoEntidadUpdateView.as_view(), name='update'),
  	url(r'^delete/(?P<pk>\d+)/$', views.TipoEntidadDeleteView.as_view(), name='delete'),
]