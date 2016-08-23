# -*- encoding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.http import JsonResponse

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Menu
from .mixins import AccessUserRequiredMixin
from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets
from django.db.models import Q
import socket

class MenuMainListView(AccessUserRequiredMixin, ListView):
	model         = Menu 
	template_name = 'menu_main.html'

	def get_context_data(self, **kwarg):
	    context     = super(MenuMainListView, self).get_context_data(**kwarg)
	    is_auth  = False 
	    username = None
	    avatar   = None
	    
	    if self.request.user.is_authenticated():
	        id_usuario  = self.get_user_id()
	        is_auth     = True
	        username    = self.get_username()
	        avatar      = self.get_user_avatar()
	        total_usuarios = self.model.objects.count()

	    data = {
	        'id_usuario' : id_usuario,
	        'is_auth'    : is_auth,
	        'username'   : username,
	        'avatar'     : avatar,
	        'total_usuarios' : total_usuarios,
	    }

	    context.update(data)
	    return context

	def get_user_id(self):
	    return self.request.user.id 

	def get_username(self):
	    return self.request.user.username

	def get_user_avatar(self):
	    return self.request.user.avatar


	