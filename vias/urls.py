# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.ViaCreateView.as_view(), name='create'),
  	url(r'^list/$', views.ViaListView.as_view(), name='list'),
  	url(r'^detail/(?P<pk>\d+)/$', views.ViaDetailView.as_view(), name='detail'),
  	url(r'^update/(?P<pk>\d+)/$', views.ViaUpdateView.as_view(), name='update'),
  	url(r'^delete/(?P<pk>\d+)/$', views.ViaDeleteView.as_view(), name='delete'),
]