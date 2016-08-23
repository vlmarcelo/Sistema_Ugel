# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import EstadoCivil


class EstadoCivilSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model  = EstadoCivil
		fields = '__all__'