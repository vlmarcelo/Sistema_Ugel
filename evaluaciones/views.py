# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Evaluacion
#from .mixins import AccessUserRequiredMixin
from .forms import EvaluacionModelForm
from docentes.models import Docente
from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets
from pure_pagination.mixins import PaginationMixin
from django.db.models import Q
import socket


class EvaluacionCreateView(CreateView):
	form_class    = EvaluacionModelForm
	models        = Evaluacion
	success_url   = reverse_lazy('menu:main')
	template_name = 'evaluacion_create.html'
	
	def form_valid(self, form):
	    self.object = form.save(commit=False)
	    self.object.usuario_creador 	  = self.request.user
	    self.object.ultimo_usuario_editor = self.object.usuario_creador
	    try:
	        self.object.nombre_host = socket.gethostname()
	    except:
	       self.object.nombre_host  = 'localhost'

	    self.object.direccion_ip    = socket.gethostbyname(socket.gethostname())
	    
	    estudio_realizado = self.object.estudio_realizados.puntaje
	    curso_capacitaion_pedagogico = self.object.curso_capacitaion_pedagogico.puntaje
	    formacion_capacitacion_aspecto_cargo = self.object.formacion_capacitacion_aspecto_cargo.puntaje
	    experiencia_sector_publico = self.object.experiencia_sector_publico.puntaje
	    experiencia_trabajo_aula = self.object.experiencia_trabajo_aula.puntaje
	    experiencia_docente = self.object.experiencia_docente.puntaje
	    experiencia_asesorias_acompanamientos = self.object.experiencia_asesorias_acompanamientos.puntaje
	    experiencia_procesos_capacitaciones_formacion = self.object.experiencia_procesos_capacitaciones_formacion.puntaje

	    total_puntaje = estudio_realizado + curso_capacitaion_pedagogico + formacion_capacitacion_aspecto_cargo + experiencia_sector_publico + experiencia_trabajo_aula + experiencia_docente +experiencia_asesorias_acompanamientos + experiencia_procesos_capacitaciones_formacion

	    docente = Docente.objects.get(usuario=self.request.user)
	    
	    if int(total_puntaje) <= 10:
	    	docente.asignacion = "Profesor - Colegio Inicial - Fecha Asumir Cargo : 20/06/2016 "
	    elif int(total_puntaje) >= 11 and int(total_puntaje)<=19:
	    	docente.asignacion = "Profesor - Colegio Primaria - Fecha Asumir Cargo : 20/06/2016 "
	    elif int(total_puntaje) >= 20:
	    	docente.asignacion = "Profesor - Colegio Secundaria - Fecha Asumir Cargo : 20/06/2016 "
	    docente.save()
	    self.object.save()

	    return super(EvaluacionCreateView, self).form_valid(form)

	def get_context_data(self, **kwarg):
	    context     = super(EvaluacionCreateView, self).get_context_data(**kwarg)
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