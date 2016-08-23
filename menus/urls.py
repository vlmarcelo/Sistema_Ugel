# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^main/$', views.MenuMainListView.as_view(), name='main'),
]