# -*- encoding: utf-8 -*-
from django import forms
from .models import GradoInstruccion


class GradoInstruccionModelForm(forms.ModelForm):
	class Meta:
		model  = GradoInstruccion
		fields = ['nombre']
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'Input-Text'}),
        }