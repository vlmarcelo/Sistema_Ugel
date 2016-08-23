# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from docentes.models import Docente 
from estudios_realizados.models import EstudioRealizado
from cursos_capacitaciones_pedagogicos.models import CursoCapacitacionPedagogico
from formaciones_capacitaciones_cargos.models import FormacionCapacitacionCargo
from experiencias_sector_educativos.models import ExperienciaSectorPublico
from experiencias_trabajos_aulas.models import ExperienciaTrabajoAula
from experiencias_docentes.models import ExperienciaDocente
from experiencias_asesorias_acompanamientos_pedagogicos.models import ExperienciaAsesoriaAcompanamiento
from experiencias_procesos_capacitaciones_formaciones.models import ExperienciaProcesoCapacitacion
from usuarios.models import Usuario

from django.core.validators import validate_ipv46_address
from django.template.defaultfilters import slugify


class Evaluacion(models.Model):
	estudio_realizados 		    		     	  = models.ForeignKey(EstudioRealizado)
	curso_capacitaion_pedagogico 		 		  = models.ForeignKey(CursoCapacitacionPedagogico)
	formacion_capacitacion_aspecto_cargo  		  = models.ForeignKey(FormacionCapacitacionCargo)
	experiencia_sector_publico 			  		  = models.ForeignKey(ExperienciaSectorPublico)
	experiencia_trabajo_aula    		  		  = models.ForeignKey(ExperienciaTrabajoAula)
	experiencia_docente 				  		  = models.ForeignKey(ExperienciaDocente)
	experiencia_asesorias_acompanamientos 		  = models.ForeignKey(ExperienciaAsesoriaAcompanamiento)
	experiencia_procesos_capacitaciones_formacion = models.ForeignKey(ExperienciaProcesoCapacitacion)

	fecha_registro 			   		= models.DateTimeField(auto_now_add=True, auto_now=False)
	usuario_creador          	 	= models.ForeignKey(Usuario)
	fecha_ultima_actualizacion 		= models.DateTimeField(auto_now_add=False, auto_now=True) 
	ultimo_usuario_editor			= models.ForeignKey(Usuario, related_name='evaluacion_usuario_editor')
	nombre_host				    	= models.CharField(max_length=255)
	direccion_ip			    	= models.GenericIPAddressField(validators=[validate_ipv46_address])	#Método

	#Métodos
	def __unicode__(self):
		return self.estudio_realizados
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Evaluaciones'
		#Ordenar los registros por un campo especifico
		ordering = ('estudio_realizados',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Evaluacion' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Evaluaciones'



