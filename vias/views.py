# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Via
from .mixins import AccessUserRequiredMixin
from .forms import ViaModelForm
from .serializers import ViaSerializer

from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets
from pure_pagination.mixins import PaginationMixin
from django.db.models import Q
import socket


class ViaCreateView(AccessUserRequiredMixin, CreateView):
	form_class    = ViaModelForm
	models        = Via
	success_url   = reverse_lazy('via:list')
	template_name = 'via_create.html'
	
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

	    return super(ViaCreateView, self).form_valid(form)

	def get_context_data(self, **kwarg):
	    context     = super(ViaCreateView, self).get_context_data(**kwarg)
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


class ViaUpdateView(AccessUserRequiredMixin, UpdateView):
    form_class      = ViaModelForm
    models          = Via
    success_url     = reverse_lazy('via:list')
    template_name   = 'via_update.html'
    queryset        = Via.objects.all()

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

	    return super(ViaUpdateView, self).form_valid(form)

    def get_context_data(self, **kwarg):
        context     = super(ViaUpdateView, self).get_context_data(**kwarg)
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


class ViaDeleteView(AccessUserRequiredMixin, DeleteView):
    models        = Via
    queryset      = Via.objects.all()
    success_url   = reverse_lazy('via:list')
    template_name = 'via_delete.html'

    def get_context_data(self, **kwarg):
        context     = super(ViaDeleteView, self).get_context_data(**kwarg)
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


class ViaDetailView(AccessUserRequiredMixin, DetailView):
    model = Via 
    template_name = 'via_detail.html'

    def get_context_data(self, **kwarg):
        context     = super(ViaDetailView, self).get_context_data(**kwarg)
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


class ViaListView(AccessUserRequiredMixin, PaginationMixin, ListView):
    template_name = 'via_list.html'
    model         = Via # Al usar el mixin se usa object
    paginate_by   = 20

    def get_context_data(self, **kwarg):
        context     = super(ViaListView, self).get_context_data(**kwarg)
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
            return super(ViaListView, self).get(self, request, *args, **kwargs)

    def json_to_response(self):
        data = [{
            'id'        : via.id,
            'nombre'    : via.nombre,
        } for via in self.object_list]
        return JsonResponse(ViaListView, safe=False)

    def get_queryset(self):
        if self.kwargs.get('variable'):
            queryset = self.model.objects.filter(slug__icontains=self.kwargs['variable'])

        elif self.request.GET.get('buscar', ''):
            queryset = self.model.objects.filter(
                        Q(slug__icontains=self.request.GET.get('buscar', '')) 
                        |Q(pk__icontains=self.request.GET.get('buscar', '')) 
                    )
        else:
            queryset = super(ViaListView, self).get_queryset()
        return queryset

	   
class ViaViewSet(viewsets.ModelViewSet):
    model            = Via 
    serializer_class = ViaSerializer
    queryset         = Via.objects.all()