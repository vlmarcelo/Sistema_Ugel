# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.ProfesionCreateView.as_view(), name='create'),
  	url(r'^list/$', views.ProfesionListView.as_view(), name='list'),
  	url(r'^update/(?P<pk>\d+)/$', views.ProfesionUpdateView.as_view(), name='update'),
  	url(r'^delete/(?P<pk>\d+)/$', views.ProfesionDeleteView.as_view(), name='delete'),
]