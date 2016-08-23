# -*- encoding: utf-8 -*-
from django import forms
from .models import EstadoCivil


class EstadoCivilModelForm(forms.ModelForm):
	class Meta:
		model  = EstadoCivil
		fields = ['nombre']
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'Input-Text'}),
        }