# -*- encoding: utf-8 -*-
from django import forms
from .models import Zona


class ZonaModelForm(forms.ModelForm):
	class Meta:
		model  = Zona
		fields = ['nombre']
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'Input-Text'}),
        }