from django.contrib import admin
# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import ExperienciaAsesoriaAcompanamiento


@admin.register(ExperienciaAsesoriaAcompanamiento)
class ExperienciaAsesoriaAcompanamientoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'slug','fecha_registro', 'usuario_creador', 'fecha_ultima_actualizacion', 'ultimo_usuario_editor', 
						'nombre_host', 'direccion_ip')			   
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = ExperienciaAsesoriaAcompanamiento