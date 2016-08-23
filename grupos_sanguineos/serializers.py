# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import GrupoSanguineo


class GrupoSanguineoSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model  = GrupoSanguineo
		fields = '__all__'