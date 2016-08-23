# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import DocumentoIdentificacion


@admin.register(DocumentoIdentificacion)
class DocumentoIdentificacionAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'fecha_registro', 'usuario_creador', 'fecha_ultima_actualizacion', 'ultimo_usuario_editor', 
						'nombre_host', 'direccion_ip')
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = DocumentoIdentificacion
