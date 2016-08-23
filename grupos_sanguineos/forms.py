# -*- encoding: utf-8 -*-
from django import forms
from .models import GrupoSanguineo


class GrupoSanguineoModelForm(forms.ModelForm):
	class Meta:
		model  = GrupoSanguineo
		fields = ['nombre']
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'Input-Text'}),
        }