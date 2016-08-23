# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import TipoPersona


class TipoPersonaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = TipoPersona
		fields = '__all__'