# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from usuarios.models import Usuario 
from django.core.validators import validate_ipv46_address
from django.template.defaultfilters import slugify
import socket


class Pregunta(models.Model):
	#Atributos
	numero 							= models.PositiveIntegerField(unique=True)
	pregunta   						= models.CharField(max_length=255, unique=True, help_text='Escribir pregunta.')
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True)
	fecha_registro 			   		= models.DateTimeField(auto_now_add=True, auto_now=False)
	usuario_creador          	 	= models.ForeignKey(Usuario)
	fecha_ultima_actualizacion 		= models.DateTimeField(auto_now_add=False, auto_now=True) 
	ultimo_usuario_editor			= models.ForeignKey(Usuario, related_name='pregunta_usuario_editor')
	nombre_host				    	= models.CharField(max_length=255)
	direccion_ip			    	= models.GenericIPAddressField(validators=[validate_ipv46_address])	#Método

	#Esto es cuando en la vista no existe un commit=false
	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.pregunta)
		super(Pregunta, self).save(*args, **kwargs)

	#Métodos
	def __unicode__(self):
		return self.pregunta
		
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Preguntas'
		#Ordenar los registros por un campo especifico
		ordering = ('pregunta',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Pregunta' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Preguntas'