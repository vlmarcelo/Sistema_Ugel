# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^cuestionario/$', views.EvaluacionCreateView.as_view(), name='create'),
]