# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Via


class ViaSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model  = Via
		fields = '__all__'