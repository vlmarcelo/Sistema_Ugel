# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Docente
import socket

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
	list_display   = (
					  'apellido_paterno', 'apellido_materno', 'nombre', 'documento_identificacion', 'numero_documento_identificacion',

					  'fecha_registro', 'usuario_creador', 'fecha_ultima_actualizacion', 'ultimo_usuario_editor',
					  'nombre_host', 'direccion_ip', 
					 )
	list_instances = True
	search_fields  = ('nombre', )

	class Meta:
		model = Docente