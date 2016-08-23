# -*- encoding: utf-8 -*-
from django import forms
from .models import ClaseEntidad


class ClaseEntidadModelForm(forms.ModelForm):
	class Meta:
		model  = ClaseEntidad
		fields = ['nombre']
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'Input-Text'}),
        }