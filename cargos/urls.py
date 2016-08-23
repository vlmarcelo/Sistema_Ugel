# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.CargoCreateView.as_view(), name='create'),
  	url(r'^list/$', views.CargoListView.as_view(), name='list'),
  	url(r'^detail/(?P<pk>\d+)/$', views.CargoDetailView.as_view(), name='detail'),
  	url(r'^update/(?P<pk>\d+)/$', views.CargoUpdateView.as_view(), name='update'),
  	url(r'^delete/(?P<pk>\d+)/$', views.CargoDeleteView.as_view(), name='delete'),
]