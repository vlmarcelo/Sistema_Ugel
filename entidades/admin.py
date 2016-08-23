# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Entidad
import socket

@admin.register(Entidad)
class EntidadAdmin(admin.ModelAdmin):
	list_display   = (
					  'clase_entidad', 'tipo_entidad', 'nombre','siglas', 'documento_identificacion', 
					  'numero_documento_identificacion', 'mision', 'vision', 
					  'fecha_creacion', 'fecha_cese', 'descripcion', 'observacion', 'logotipo', 'slug', 
					  'fecha_registro', 'usuario_creador', 'fecha_ultima_actualizacion', 'ultimo_usuario_editor',
					  'nombre_host', 'direccion_ip', 
					 )
	list_instances = True
	search_fields  = ('nombre', 'numero_documento_identificacion')

	class Meta:
		model = Entidad