# -*- encoding: utf-8 -*-
from django import forms
from .models import Pais


class PaisModelForm(forms.ModelForm):
	class Meta:
		model  = Pais
		fields = ['nombre', 'codigo_postal', 'descripcion', 'imagen']
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'Input-Text'}),
			'codigo_postal'	  : forms.TextInput(attrs={'class':'Input-Text'}),
            'descripcion': forms.Textarea(attrs={'class':'Input-Area', }),
            'imagen'  : forms.FileInput(attrs={'class':'InputFile'}),
        }




