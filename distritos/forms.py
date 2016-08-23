# -*- encoding: utf-8 -*-
from django import forms
from .models import Distrito


class DistritoModelForm(forms.ModelForm):
	class Meta:
		model  = Distrito
		fields = ['provincia', 'nombre', 'descripcion', 'imagen']
		widgets = {
			#'pais'	: forms.ChoiceField(),
			'provincia': forms.Select(attrs={'class':'Select'}),
			'nombre': forms.TextInput(attrs={'class':'Input-Text'}),
	        'descripcion': forms.Textarea(attrs={'class':'Input-Area', }),
            'imagen'  : forms.FileInput(attrs={'class':'InputFile'}),
        }

