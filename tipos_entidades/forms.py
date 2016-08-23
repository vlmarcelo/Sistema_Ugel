# -*- encoding: utf-8 -*-
from django import forms
from .models import TipoEntidad


class TipoEntidadModelForm(forms.ModelForm):
	class Meta:
		model  = TipoEntidad
		fields = ['nombre']
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'Input-Text'}),
        }