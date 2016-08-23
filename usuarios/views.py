# -*- encoding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.models import Group, Permission

from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters

from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import FormView
from django.views.generic import TemplateView
from django.views.generic import View
from django.views.generic import RedirectView

from braces.views import LoginRequiredMixin, RecentLoginRequiredMixin

from .models import Usuario
from .serializers import UsuarioSerializer, PermissionSerializer, GroupSerializer
from .mixins import ExcelExportView, CsvExportView, AccessUserRequiredMixin
from .forms import UsuarioModelForm, UserCreationEmailForm, UsuarioAuthenticationForm

from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets
from django.db.models import Q
from django.core.mail import EmailMultiAlternatives
import socket


class LoginView(FormView):
    form_class    =  UsuarioAuthenticationForm
    template_name = 'index.html'
    success_url   =  reverse_lazy('menu:main')

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid(form)

    @method_decorator(sensitive_post_parameters('password'))
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)


class LogoutView(RedirectView):
    url = reverse_lazy('usuario:login')
    def get(self, request, *args, **kwargs):
        auth_logout(self.request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class UsuarioCreateView(CreateView):
    models        = Usuario 
    template_name = 'usuario_create.html'
    form_class    = UsuarioModelForm
    success_url   = reverse_lazy('menu:main')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(form.cleaned_data['password'])
        self.object.slug = self.object.username
        try:
            self.object.nombre_host = socket.gethostname()
        except:
           self.object.nombre_host  = 'localhost'

        self.object.direccion_ip    = socket.gethostbyname(socket.gethostname())
        
        to_admin = self.object.email 
        html_content = 'Su usuario ha sido activado. Sistema UGEL'
        msg = EmailMultiAlternatives('Correo:', html_content, 'from@server.com',[to_admin])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
        self.object.save()

        return super(UsuarioCreateView, self).form_valid(form)


class UsuarioDetailView(AccessUserRequiredMixin, DetailView):
    model = Usuario 
    template_name = 'usuario_detail.html'

    def get_context_data(self, **kwarg):
        context     = super(UsuarioDetailView, self).get_context_data(**kwarg)
        is_auth  = False 
        username = None
        avatar   = None

        if self.request.user.is_authenticated():
            id_usuario  = self.get_user_id()
            is_auth     = True
            username    = self.get_username()
            avatar      = self.get_user_avatar()

        data = {
            'id_usuario' : id_usuario,
            'is_auth'    : is_auth,
            'username'   : username,
            'avatar'     : avatar,
        }

        context.update(data)
        return context

    def get_user_id(self):
        return self.request.user.id 

    def get_username(self):
        return self.request.user.username

    def get_user_avatar(self):
        return self.request.user.avatar


class UsuarioUpdateView(AccessUserRequiredMixin, UpdateView):
    form_class      = UsuarioModelForm
    models          = Usuario
    success_url     = reverse_lazy('usuario:list')
    template_name   = 'usuario_update.html'
    queryset        = Usuario.objects.all()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(form.cleaned_data['password'])
        self.object.slug = self.object.username
        try:
            self.object.nombre_host = socket.gethostname()
        except:
           self.object.nombre_host  = 'localhost'

        self.object.direccion_ip    = socket.gethostbyname(socket.gethostname())
        self.object.save()

        return super(UsuarioUpdateView, self).form_valid(form)

    def get_context_data(self, **kwarg):
        context     = super(UsuarioUpdateView, self).get_context_data(**kwarg)
        is_auth  = False 
        username = None
        avatar   = None

        if self.request.user.is_authenticated():
            id_usuario  = self.get_user_id()
            is_auth     = True
            username    = self.get_username()
            avatar      = self.get_user_avatar()
            

        data = {
            'id_usuario' : id_usuario,
            'is_auth'    : is_auth,
            'username'   : username,
            'avatar'     : avatar,
           
        }

        context.update(data)
        return context

    def get_user_id(self):
        return self.request.user.id 

    def get_username(self):
        return self.request.user.username

    def get_user_avatar(self):
        return self.request.user.avatar


class UsuarioDeleteView(AccessUserRequiredMixin, DeleteView):
    models        = Usuario
    queryset      = Usuario.objects.all()
    success_url   = reverse_lazy('usuario:list')
    template_name = 'usuario_delete.html'

    def get_context_data(self, **kwarg):
        context     = super(UsuarioDeleteView, self).get_context_data(**kwarg)
        is_auth  = False 
        username = None
        avatar   = None

        if self.request.user.is_authenticated():
            id_usuario  = self.get_user_id()
            is_auth     = True
            username    = self.get_username()
            avatar      = self.get_user_avatar()

        data = {
            'id_usuario' : id_usuario,
            'is_auth'    : is_auth,
            'username'   : username,
            'avatar'     : avatar,
        }

        context.update(data)
        return context

    def get_user_id(self):
        return self.request.user.id 

    def get_username(self):
        return self.request.user.username

    def get_user_avatar(self):
        return self.request.user.avatar
