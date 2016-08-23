# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Departamento


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model  = Departamento
		fields = '__all__'