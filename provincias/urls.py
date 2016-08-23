# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.ProvinciaCreateView.as_view(), name='create'),
  	url(r'^list/$', views.ProvinciaListView.as_view(), name='list'),
  	url(r'^detail/(?P<pk>\d+)/$', views.ProvinciaDetailView.as_view(), name='detail'),
  	url(r'^update/(?P<pk>\d+)/$', views.ProvinciaUpdateView.as_view(), name='update'),
  	url(r'^delete/(?P<pk>\d+)/$', views.ProvinciaDeleteView.as_view(), name='delete'),
]