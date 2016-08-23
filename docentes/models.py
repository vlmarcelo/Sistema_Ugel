# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from personas.models import Persona 
from cargos.models import Cargo 
from grados_instrucciones.models import GradoInstruccion
from tipos_docentes.models import TipoDocente
from profesiones.models import Profesion 
from ocupaciones.models import Ocupacion
from usuarios.models import Usuario
from idiomas.models import Idioma
from entidades.models import Entidad
from django.core.validators import validate_ipv46_address
from django.template.defaultfilters import slugify


class Docente(Persona):
	usuario							= models.OneToOneField(Usuario, unique=True)
	entidad 						= models.ForeignKey(Entidad)
	tipo_docente    				= models.ForeignKey(TipoDocente)
	cargo 	  				    	= models.ForeignKey(Cargo)
	grado_instruccion 				= models.ForeignKey(GradoInstruccion) 
	profesion 		  				= models.ForeignKey(Profesion)
	ocupacion 		  				= models.ForeignKey(Ocupacion)
	idioma 							= models.ForeignKey(Idioma)		
	ano_experiencia					= models.PositiveSmallIntegerField(default=0, help_text='Escribir año(s) de experiencia(s).')
	ano_experiencia_docente			= models.PositiveSmallIntegerField(default=0, help_text='Escribir año(s) de experiencia(s) como docente.')	
	ano_experiencia_docente_materia = models.PositiveSmallIntegerField(default=0, help_text='Escribir año(s) de experiencia(s) como docente en materia.')	
	email_corporativo				= models.EmailField(blank=True, null=True, max_length=255, help_text="Escribir E-Mail Corporativo.")	
	fecha_inicio_contratacion 		= models.DateField(help_text="Seleccionar fecha de inicio de contratación del empleado.")
	fecha_fin_contratacion 			= models.DateField(blank=True, null=True, help_text="Seleccionar fecha de final de contratación del empleado.")
	
	fecha_cese						= models.DateTimeField(blank=True, null=True, help_text="Seleccionar fecha de cese del empleado.")
	descripcion		    			= models.TextField(blank=True, null=True, help_text='Escribir descripción del empleado (Opcional).')
	observacion		   				= models.TextField(blank=True, null=True, help_text='Escribir observación del empleado (Opcional).') 
	
	asignacion 						= models.TextField(blank=True, null=True)
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True)
	fecha_registro 			   		= models.DateTimeField(auto_now_add=True, auto_now=False)
	usuario_creador          	 	= models.ForeignKey(Usuario, related_name='empleado_usuario_creador')
	fecha_ultima_actualizacion 		= models.DateTimeField(auto_now_add=False, auto_now=True) 
	ultimo_usuario_editor			= models.ForeignKey(Usuario, related_name='empleado_usuario_editor')
	nombre_host				    	= models.CharField(max_length=255)
	direccion_ip			    	= models.GenericIPAddressField(validators=[validate_ipv46_address])	#Métodos
	

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_nombre_completo())
		super(Docente, self).save(*args, **kwargs)
		
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Docentes'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Docente' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Docentes'#Métodos

	
