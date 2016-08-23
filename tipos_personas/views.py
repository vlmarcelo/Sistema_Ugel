# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import TipoPersona
from .serializers import TipoPersonaSerializer


class TipoPersonaViewSet(viewsets.ModelViewSet):
    model            = TipoPersona 
    serializer_class = TipoPersonaSerializer
    queryset         = TipoPersona.objects.all()
