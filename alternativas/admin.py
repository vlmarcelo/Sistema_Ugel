# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Alternativa


@admin.register(Alternativa)
class AlternativaAdmin(admin.ModelAdmin):
	list_display   = ('pregunta', 'alternativa', 'puntaje',
					  'slug', 'fecha_registro', 'usuario_creador', 'fecha_ultima_actualizacion', 
					  'ultimo_usuario_editor', 'nombre_host', 'direccion_ip')
	list_instances = True
	search_fields  = ('alternativa',)

	class Meta:
		model = Alternativa