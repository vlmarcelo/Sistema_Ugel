# -*- encoding: utf-8 -*-
from django import forms
from .models import Provincia


class ProvinciaModelForm(forms.ModelForm):
	class Meta:
		model  = Provincia
		fields = ['departamento', 'nombre', 'descripcion', 'imagen']
		widgets = {
			#'pais'	: forms.ChoiceField(),
			'departamento': forms.Select(attrs={'class':'Select'}),
			'nombre': forms.TextInput(attrs={'class':'Input-Text'}),
	        'descripcion': forms.Textarea(attrs={'class':'Input-Area', }),
            'imagen'  : forms.FileInput(attrs={'class':'InputFile'}),
        }

