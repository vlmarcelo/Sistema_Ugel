# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from usuarios.models import Usuario 

from django.core.validators import validate_ipv46_address
from django.template.defaultfilters import slugify
import socket


class Pais(models.Model):
	#Atributos
	nombre   						= models.CharField(max_length=255, unique=True, help_text='Escribir nombre del país.')
	codigo_postal  					= models.PositiveIntegerField(verbose_name='Código postal', unique=True, help_text='Escribir nombre del país.')
	imagen 		   					= models.ImageField(blank=True, 
														upload_to='imagenes_paises', 
														default='default/No-Image-1.png',
														help_text='Subir imagen del país. (Opcional)')

	descripcion    					= models.TextField(blank=True, help_text='Escribir descripción del país. (Opcional)')
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True)
	fecha_registro 			   		= models.DateTimeField(auto_now_add=True, auto_now=False)
	usuario_creador          	 	= models.ForeignKey(Usuario)
	fecha_ultima_actualizacion 		= models.DateTimeField(auto_now_add=False, auto_now=True) 
	ultimo_usuario_editor			= models.ForeignKey(Usuario, related_name='pais_usuario_editor')
	nombre_host				    	= models.CharField(max_length=255)
	direccion_ip			    	= models.GenericIPAddressField(validators=[validate_ipv46_address])	#Método

	#Esto es cuando en la vista no existe un commit=false
	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.nombre)
		super(Pais, self).save(*args, **kwargs)

	#Métodos
	def __unicode__(self):
		return self.nombre
		
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Paises'
		#Ordenar los registros por un campo especifico
		ordering = ('nombre',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'País' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Paises'