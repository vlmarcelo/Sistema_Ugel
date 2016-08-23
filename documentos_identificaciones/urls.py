# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.DocumentoIdentificacionCreateView.as_view(), name='create'),
  	url(r'^list/$', views.DocumentoIdentificacionListView.as_view(), name='list'),
  	url(r'^detail/(?P<pk>\d+)/$', views.DocumentoIdentificacionDetailView.as_view(), name='detail'),
  	url(r'^update/(?P<pk>\d+)/$', views.DocumentoIdentificacionUpdateView.as_view(), name='update'),
  	url(r'^delete/(?P<pk>\d+)/$', views.DocumentoIdentificacionDeleteView.as_view(), name='delete'),
]