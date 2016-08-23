# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^nuevo/$', views.PaisCreateView.as_view(), name='create'),
  	url(r'^list/$', views.PaisListView.as_view(), name='list'),
  	url(r'^detail/(?P<pk>\d+)/$', views.PaisDetailView.as_view(), name='detail'),
  	url(r'^update/(?P<pk>\d+)/$', views.PaisUpdateView.as_view(), name='update'),
  	url(r'^delete/(?P<pk>\d+)/$', views.PaisDeleteView.as_view(), name='delete'),
]