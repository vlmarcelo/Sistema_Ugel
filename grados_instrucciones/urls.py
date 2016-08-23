# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.GradoInstruccionCreateView.as_view(), name='create'),
  	url(r'^list/$', views.GradoInstruccionListView.as_view(), name='list'),
  	url(r'^update/(?P<pk>\d+)/$', views.GradoInstruccionUpdateView.as_view(), name='update'),
  	url(r'^delete/(?P<pk>\d+)/$', views.GradoInstruccionDeleteView.as_view(), name='delete'),
]