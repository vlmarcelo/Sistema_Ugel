# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^inscripcion/$', views.DocenteCreateView.as_view(), name='create'),
	url(r'^list/$', views.DocenteListView.as_view(), name='list'),
	url(r'^detalle/(?P<pk>\d+)/$', views.DocenteDetailView.as_view(), name='detail'),
  	url(r'^actualizar/(?P<pk>\d+)/$', views.DocenteUpdateView.as_view(), name='update'),
]