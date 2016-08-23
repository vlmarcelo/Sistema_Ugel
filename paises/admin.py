# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Pais


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
	list_display   = ('nombre', 'codigo_postal', 'imagen', 'descripcion', 
					  'slug', 'fecha_registro', 'usuario_creador', 'fecha_ultima_actualizacion', 
					  'ultimo_usuario_editor', 'nombre_host', 'direccion_ip')
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Pais

#admin.site.register(Pais, PaisAdmin)