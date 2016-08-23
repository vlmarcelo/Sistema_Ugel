# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Profesion


class ProfesionSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model  = Profesion
		fields = '__all__'