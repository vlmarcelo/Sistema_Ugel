# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from usuarios.models import Usuario 
from preguntas.models import Pregunta
from alternativas.models import Alternativa
from docentes.models import Docente
from django.core.validators import validate_ipv46_address
from django.template.defaultfilters import slugify
import socket


class Cuestionario(models.Model):
	#Atributos
	alternativa						= models.OneToOneField(Alternativa)
	docente 						= models.OneToOneField(Docente)
	
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True)
	fecha_registro 			   		= models.DateTimeField(auto_now_add=True, auto_now=False)
	usuario_creador          	 	= models.ForeignKey(Usuario)
	fecha_ultima_actualizacion 		= models.DateTimeField(auto_now_add=False, auto_now=True) 
	ultimo_usuario_editor			= models.ForeignKey(Usuario, related_name='cuestionario_usuario_editor')
	nombre_host				    	= models.CharField(max_length=255)
	direccion_ip			    	= models.GenericIPAddressField(validators=[validate_ipv46_address])	#Método

	#Esto es cuando en la vista no existe un commit=false
	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_valor_ano_uit_fiscal())
		super(Cuestionario, self).save(*args, **kwargs)
	#Métodos
	def __unicode__(self):
		return self.get_valor_ano_uit_fiscal()

	def get_valor_ano_uit_fiscal(self):
		return 'Docente: %s - Alternativa: %s' %(self.docente, self.alternativa)


	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Cuestionarios'
		#Ordenar los registros por un campo especifico
		ordering = ('docente',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Cuestionario' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Cuestionarios'