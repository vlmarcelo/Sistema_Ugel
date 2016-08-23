# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Cuestionario


@admin.register(Cuestionario)
class CuestionarioAdmin(admin.ModelAdmin):
	list_display   = (
					  'slug', 'fecha_registro', 'usuario_creador', 'fecha_ultima_actualizacion', 
					  'ultimo_usuario_editor', 'nombre_host', 'direccion_ip')
	list_instances = True


	class Meta:
		model = Cuestionario

#admin.site.register(Pais, PaisAdmin)