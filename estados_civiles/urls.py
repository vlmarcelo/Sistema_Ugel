# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.EstadoCivilCreateView.as_view(), name='create'),
  	url(r'^list/$', views.EstadoCivilListView.as_view(), name='list'),
  	url(r'^detail/(?P<pk>\d+)/$', views.EstadoCivilDetailView.as_view(), name='detail'),
  	url(r'^update/(?P<pk>\d+)/$', views.EstadoCivilUpdateView.as_view(), name='update'),
  	url(r'^delete/(?P<pk>\d+)/$', views.EstadoCivilDeleteView.as_view(), name='delete'),
]