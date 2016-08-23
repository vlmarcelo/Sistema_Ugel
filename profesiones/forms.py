# -*- encoding: utf-8 -*-
from django import forms
from .models import Profesion


class ProfesionModelForm(forms.ModelForm):
	class Meta:
		model  = Profesion
		fields = ['nombre']
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'Input-Text'}),
        }