
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from distritos.models import Distrito 
from documentos_identificaciones.models import DocumentoIdentificacion
from estados_civiles.models import EstadoCivil
from grupos_sanguineos.models import GrupoSanguineo
from usuarios.models import Usuario
from vias.models import Via 
from zonas.models import Zona 
from tipos_personas.models import TipoPersona
from django.core.validators import validate_ipv46_address
from django.template.defaultfilters import slugify

class Persona(models.Model):

	BOOL_HIJO 		 				= ((True, 'Si'), (False, "No"))
	BOOL_GENERO 	 				= ((True, 'Masculino'), (False, "Femenino"))
		
	tipo_persona 					= models.ForeignKey(TipoPersona, default=1, help_text='Seleccionar tipo de persona.', related_name='%(app_label)s_%(class)s_related')
	apellido_paterno 		 		= models.CharField(max_length=255, help_text='Escribir apellido paterno.', db_index=True)
	apellido_materno 		 		= models.CharField(max_length=255, help_text='Escribir apellido materno.', db_index=True)
	nombre 			 		 		= models.CharField(max_length=255, help_text='Escribir nombre(s).', db_index=True)
	documento_identificacion 		= models.ForeignKey(DocumentoIdentificacion, verbose_name='Documento identificación', on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related')
	numero_documento_identificacion = models.CharField(verbose_name='Número Documento identificación', unique=True, max_length=30, help_text='Escribir número documento identificación.', db_index=True)
	fecha_nacimiento			    = models.DateField(default='01/01/1980')
	genero 							= models.BooleanField(verbose_name='Género', choices=BOOL_GENERO, default=True)
	estado_civil 					= models.ForeignKey(EstadoCivil, related_name='%(app_label)s_%(class)s_related')
	grupo_sanguineo 				= models.ForeignKey(GrupoSanguineo, verbose_name='Grupo sanguíneo', related_name='%(app_label)s_%(class)s_related')
	fotografia   					= models.ImageField(blank=True, 
														null=True, 
														verbose_name='Fotografía',
														upload_to='fotografia',
														default='default/No-Image-1.png',
														help_text='Subir fotografia (Opcional).',
														)
	hijo							= models.BooleanField(verbose_name='¿Hijo(s)?', choices=BOOL_HIJO, default=False)
	numero_hijo						= models.PositiveSmallIntegerField(default=0, help_text='Escribir número(s) de hijo(s).')
	observacion_persona 			= models.TextField(blank=True, help_text='Escribir observación de la persona (Opcional).')
	distrito 						= models.ForeignKey(Distrito, related_name='%(app_label)s_%(class)s_related')
	zona							= models.ForeignKey(Zona, related_name='%(app_label)s_%(class)s_related')
	via								= models.ForeignKey(Via, related_name='%(app_label)s_%(class)s_related')
	nombre_direccion				= models.CharField(max_length=255, help_text='Escribir nombre de la dirección.')
	edificio						= models.CharField(blank=True, max_length=20, null=True)
	departamento					= models.CharField(blank=True, max_length=20, null=True)
	apartamento						= models.CharField(blank=True, max_length=20, null=True)
	pabellon						= models.CharField(blank=True, max_length=20, null=True)
	bloque 							= models.CharField(blank=True, max_length=20, null=True)
	piso 							= models.CharField(blank=True, max_length=20, null=True)
	interior						= models.CharField(blank=True, max_length=20, null=True)
	pasadizo 						= models.CharField(blank=True, max_length=20, null=True)
	numero 							= models.CharField(blank=True, max_length=20, null=True)
	cuadra							= models.CharField(blank=True, max_length=20, null=True)
	manzana							= models.CharField(blank=True, max_length=20, null=True)
	etapa							= models.CharField(blank=True, max_length=20, null=True)
	lote							= models.CharField(blank=True, max_length=20, null=True)
	sub_lote						= models.CharField(blank=True, max_length=20, null=True)
	sector 							= models.CharField(blank=True, max_length=20, null=True)
	kilometro						= models.CharField(blank=True, max_length=20, null=True)
	denominacion					= models.CharField(blank=True, max_length=255, null=True, help_text='Escribir denominación (Opcional).')
	referencia						= models.CharField(blank=True, max_length=255, null=True, help_text='Escribir referencia (Opcional).')
	observacion_direccion			= models.CharField(blank=True, max_length=255, null=True, help_text='Escribir observación de la dirección (Opcional).')
	telefono_personal				= models.CharField(blank=True, max_length=30, help_text='Escribir número de teléfono personal (Opcional).', null=True)
	celular_personal				= models.CharField(blank=True, max_length=30, help_text='Escribir número de celular personal (Opcional).', null=True)
	email_personal					= models.EmailField(blank=True, max_length=255, help_text='Escribir E-Mail (Opcional).', null=True)
	
	def __unicode__(self):
		return self.get_nombre_completo()

	def get_nombre_completo(self):
		return self.apellido_paterno + ' ' + self.apellido_materno + ', ' + self.nombre

	class Meta:
		abstract = True