# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Ocupacion


class OcupacionSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model  = Ocupacion
		fields = '__all__'