# -*- encoding: utf-8 -*-
from django import forms
from .models import Departamento


class DepartamentoModelForm(forms.ModelForm):

	class Meta:
		model  = Departamento
		fields = ['pais', 'nombre', 'codigo_postal', 'descripcion', 'imagen']
		widgets = {
			#'pais'	: forms.ChoiceField(),
			'pais': forms.Select(attrs={'class':'Select'}),
			'nombre': forms.TextInput(attrs={'class':'Input-Text'}),
			'codigo_postal'	  : forms.TextInput(attrs={'class':'Input-Text'}),
            'descripcion': forms.Textarea(attrs={'class':'Input-Area', }),
            'imagen'  : forms.FileInput(attrs={'class':'InputFile'}),
        }



