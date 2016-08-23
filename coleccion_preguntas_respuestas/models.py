# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from usuarios.models import Usuario 
from preguntas.models import Pregunta
from respuestas.models import Respuesta

from django.core.validators import validate_ipv46_address
from django.template.defaultfilters import slugify
import socket


class ColeccionPreguntaRespuesta(models.Model):
	#Atributos
	pregunta						= models.ForeignKey(Pregunta)
	respuesta						= models.ForeignKey(Respuesta)
	check 							= models.BooleanField(default=False)
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True)
	fecha_registro 			   		= models.DateTimeField(auto_now_add=True, auto_now=False)
	usuario_creador          	 	= models.ForeignKey(Usuario)
	fecha_ultima_actualizacion 		= models.DateTimeField(auto_now_add=False, auto_now=True) 
	ultimo_usuario_editor			= models.ForeignKey(Usuario, related_name='coleccion_pregunta_respuesta_usuario_editor')
	nombre_host				    	= models.CharField(max_length=255)
	direccion_ip			    	= models.GenericIPAddressField(validators=[validate_ipv46_address])	#Método

	#Esto es cuando en la vista no existe un commit=false
	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_valor_ano_uit_fiscal())
		super(ColeccionPreguntaRespuesta, self).save(*args, **kwargs)
	#Métodos
	def __unicode__(self):
		return self.get_valor_ano_uit_fiscal()

	def get_valor_ano_uit_fiscal(self):
		return 'Pregunta: %s - Respuesta: %s' %(self.pregunta, self.respuesta)


	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Colecciones_Preguntas_Respuestas'
		#Ordenar los registros por un campo especifico
		ordering = ('pregunta',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Coleccion Pregunta Respuesta' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Colecciones Preguntas Respuestas'