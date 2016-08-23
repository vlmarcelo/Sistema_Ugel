# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from usuarios.models import Usuario 
from preguntas.models import Pregunta
from django.core.validators import validate_ipv46_address
from django.template.defaultfilters import slugify
import socket


class Alternativa(models.Model):
	#Atributos
	alternativa   					= models.CharField(max_length=255, unique=True, help_text='Escribir alternativa.')
	pregunta 						= models.ForeignKey(Pregunta)
	puntaje 						= models.PositiveIntegerField(default=0)
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True)
	fecha_registro 			   		= models.DateTimeField(auto_now_add=True, auto_now=False)
	usuario_creador          	 	= models.ForeignKey(Usuario)
	fecha_ultima_actualizacion 		= models.DateTimeField(auto_now_add=False, auto_now=True) 
	ultimo_usuario_editor			= models.ForeignKey(Usuario, related_name='alternativa_usuario_editor')
	nombre_host				    	= models.CharField(max_length=255)
	direccion_ip			    	= models.GenericIPAddressField(validators=[validate_ipv46_address])	#Método

	#Esto es cuando en la vista no existe un commit=false
	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.alternativa)
		super(Alternativa, self).save(*args, **kwargs)

	#Métodos
	def __unicode__(self):
		return self.alternativa
		
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Alternativas'
		#Ordenar los registros por un campo especifico
		ordering = ('alternativa',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Alternativa' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Alternativas'