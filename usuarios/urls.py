# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.LoginView.as_view(), name='login'),
	url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
	url(r'^nuevo/$', views.UsuarioCreateView.as_view(), name='create'),
	url(r'^actualizar/(?P<pk>\d+)/$', views.UsuarioUpdateView.as_view(), name='update'),
	url(r'^detalle/(?P<pk>\d+)/$', views.UsuarioDetailView.as_view(), name='detail'),
]