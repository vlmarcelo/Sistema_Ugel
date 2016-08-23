# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import DocumentoIdentificacion


class DocumentoIdentificacionSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model  = DocumentoIdentificacion
		fields = '__all__'