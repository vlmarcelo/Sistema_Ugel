# -*- encoding: utf-8 -*-
from django.contrib.auth.models import Group,Permission
from rest_framework import serializers
from .models import Usuario


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Permission 
		fields = '__all__'
			

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Usuario
		fields = '__all__'