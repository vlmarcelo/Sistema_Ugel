# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Zona


class ZonaSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model  = Zona
		fields = '__all__'