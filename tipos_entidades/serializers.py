# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import TipoEntidad


class TipoEntidadSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model  = TipoEntidad
		fields = '__all__'