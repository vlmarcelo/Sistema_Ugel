# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^nuevo/$', views.EntidadCreateView.as_view(), name='create'),
    url(r'^list/$', views.EntidadListView.as_view(), name='list'),
    url(r'^update/(?P<pk>\d+)/$', views.EntidadUpdateView.as_view(), name='update'),
	url(r'^delete/(?P<pk>\d+)/$', views.EntidadDeleteView.as_view(), name='delete'),
	url(r'^detail/(?P<pk>\d+)/$', views.EntidadDetailView.as_view(), name='detail'),
]