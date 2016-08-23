# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Entidad
from .mixins import AccessUserRequiredMixin
from .forms import EntidadModelForm

from .serializers import EntidadSerializer

from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets
from pure_pagination.mixins import PaginationMixin
from django.db.models import Q
import socket


class EntidadCreateView(AccessUserRequiredMixin, CreateView):
	form_class    = EntidadModelForm
	models        = Entidad
	success_url   = reverse_lazy('entidad:list')
	template_name = 'entidad_create.html'
	
	def form_valid(self, form):
	    self.object = form.save(commit=False)
	    self.object.usuario_creador 	  = self.request.user
	    self.object.ultimo_usuario_editor = self.object.usuario_creador
	    self.object.slug = self.object.nombre
	    try:
	        self.object.nombre_host = socket.gethostname()
	    except:
	       self.object.nombre_host  = 'localhost'

	    self.object.direccion_ip    = socket.gethostbyname(socket.gethostname())
	    self.object.save()

	    return super(EntidadCreateView, self).form_valid(form)

	def get_context_data(self, **kwarg):
	    context  = super(EntidadCreateView, self).get_context_data(**kwarg)
	    is_auth  = False 
	    username = None
	    avatar   = None

	    if self.request.user.is_authenticated():
	        id_usuario  = self.get_user_id()
	        is_auth     = True
	        username    = self.get_username()
	        avatar      = self.get_user_avatar()

	    data = {
	        'id_usuario' 		: id_usuario,
	        'is_auth'    		: is_auth,
	        'username'   		: username,
	        'avatar'     		: avatar,
	    }

	    context.update(data)
	    return context

	def get_user_id(self):
	    return self.request.user.id 

	def get_username(self):
	    return self.request.user.username

	def get_user_avatar(self):
	    return self.request.user.avatar


class EntidadUpdateView(AccessUserRequiredMixin, UpdateView):
    form_class      = EntidadModelForm
    models          = Entidad
    success_url     = reverse_lazy('entidad:list')
    template_name   = 'entidad_update.html'
    queryset        = Entidad.objects.all()

    def form_valid(self, form):
	    self.object = form.save(commit=False)
	    self.object.usuario_creador 	  = self.request.user
	    self.object.ultimo_usuario_editor = self.object.usuario_creador
	    self.object.slug = self.object.nombre
	    try:
	        self.object.nombre_host = socket.gethostname()
	    except:
	       self.object.nombre_host  = 'localhost'

	    self.object.direccion_ip    = socket.gethostbyname(socket.gethostname())
	    self.object.save()

	    return super(EntidadUpdateView, self).form_valid(form)

    def get_context_data(self, **kwarg):
        context     = super(EntidadUpdateView, self).get_context_data(**kwarg)
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


class EntidadDeleteView(AccessUserRequiredMixin, DeleteView):
    models        = Entidad
    queryset      = Entidad.objects.all()
    success_url   = reverse_lazy('entidad:list')
    template_name = 'entidad_delete.html'

    def get_context_data(self, **kwarg):
        context     = super(EntidadDeleteView, self).get_context_data(**kwarg)
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


class EntidadDetailView(AccessUserRequiredMixin, DetailView):
    model = Entidad 
    template_name = 'entidad_detail.html'

    def get_context_data(self, **kwarg):
        context     = super(EntidadDetailView, self).get_context_data(**kwarg)
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


class EntidadListView(AccessUserRequiredMixin, PaginationMixin, ListView):
    template_name = 'entidad_list.html'
    model         = Entidad # Al usar el mixin se usa object
    paginate_by   = 20

    def get_context_data(self, **kwarg):
        context     = super(EntidadListView, self).get_context_data(**kwarg)
        is_auth  = False 
        username = None
        avatar   = None
        table    = None
        
        if self.request.user.is_authenticated():
            id_usuario  = self.get_user_id()
            is_auth     = True
            username    = self.get_username()
            avatar      = self.get_user_avatar()
            total		= self.model.objects.count()

        data = {
            'id_usuario' : id_usuario,
            'is_auth'    : is_auth,
            'username'   : username,
            'avatar'     : avatar,
            'total' 	 : total,
        }

        context.update(data)
        return context

    def get_user_id(self):
        return self.request.user.id 

    def get_username(self):
        return self.request.user.username

    def get_user_avatar(self):
        return self.request.user.avatar

    def get(self, request, *args, **kwargs):
        if self.request.GET.get('buscar', ''):
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            return self.render_to_response(context)
        # Toma el queryset por defecto
        elif self.request.GET.get('format', None) == 'json':
            self.object_list = self.get_queryset()
            return self.json_to_response()
        else:
            return super(EntidadListView, self).get(self, request, *args, **kwargs)

    def json_to_response(self):
        data = [{
            'id'        : entidad.id,
            'nombre'    : entidad.nombre,
        } for entidad in self.object_list]
        return JsonResponse(EntidadListView, safe=False)

    def get_queryset(self):
        if self.kwargs.get('variable'):
            queryset = self.model.objects.filter(slug__icontains=self.kwargs['variable'])

        elif self.request.GET.get('buscar', ''):
            queryset = self.model.objects.filter(
                        Q(slug__icontains=self.request.GET.get('buscar', '')) 
                        |Q(pk__icontains=self.request.GET.get('buscar', '')) 
                    )
        else:
            queryset = super(EntidadListView, self).get_queryset()
        return queryset

	   
class EntidadViewSet(viewsets.ModelViewSet):
    model            = Entidad
    serializer_class = EntidadSerializer
    queryset         = Entidad.objects.all()

    def perform_create(self, serializer):
        try:
            nombre_host = socket.gethostname()
        except:
            nombre_host  = 'localhost'

        direccion_ip = socket.gethostbyname(socket.gethostname())
        serializer.save(
                            usuario_creador       = self.request.user, 
                            ultimo_usuario_editor = self.request.user,
                            nombre_host           = nombre_host, 
                            direccion_ip          = direccion_ip
                        )