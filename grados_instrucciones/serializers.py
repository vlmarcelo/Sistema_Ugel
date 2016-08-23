# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import GradoInstruccion


class GradoInstruccionSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model  = GradoInstruccion
		fields = '__all__'