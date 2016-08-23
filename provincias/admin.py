# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Provincia


@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
	list_display   = ('departamento', 'nombre', 'imagen', 'descripcion', 
					  'slug', 'fecha_registro', 'usuario_creador', 'fecha_ultima_actualizacion', 
					  'ultimo_usuario_editor', 'nombre_host', 'direccion_ip')
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Provincia

#admin.site.register(Pais, PaisAdmin)