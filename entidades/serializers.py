# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Entidad


class EntidadSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model  = Entidad
		fields = [
					'id', 'clase_entidad', 'tipo_entidad', 'nombre', 'siglas', 'documento_identificacion', 
					'numero_documento_identificacion', 'mision', 'vision', 'logotipo', 'fecha_creacion', 
					'fecha_cese', 'descripcion', 'observacion',

				 ]