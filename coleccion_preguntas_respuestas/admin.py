# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import ColeccionPreguntaRespuesta


@admin.register(ColeccionPreguntaRespuesta)
class ColeccionPreguntaRespuestaAdmin(admin.ModelAdmin):
	list_display   = ('pregunta', 'respuesta', 'check', 
					  'slug', 'fecha_registro', 'usuario_creador', 'fecha_ultima_actualizacion', 
					  'ultimo_usuario_editor', 'nombre_host', 'direccion_ip')
	list_instances = True
	search_fields  = ('pregunta', 'respuesta')

	class Meta:
		model = ColeccionPreguntaRespuesta

#admin.site.register(Pais, PaisAdmin)