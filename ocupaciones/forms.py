# -*- encoding: utf-8 -*-
from django import forms
from .models import Ocupacion


class OcupacionModelForm(forms.ModelForm):
	class Meta:
		model  = Ocupacion
		fields = ['nombre']
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'Input-Text'}),
        }