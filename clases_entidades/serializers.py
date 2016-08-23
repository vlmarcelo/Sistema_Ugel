# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import ClaseEntidad


class ClaseEntidadSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model  = ClaseEntidad
		fields = '__all__'