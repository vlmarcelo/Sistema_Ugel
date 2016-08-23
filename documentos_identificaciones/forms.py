# -*- encoding: utf-8 -*-
from django import forms
from .models import DocumentoIdentificacion


class DocumentoIdentificacionModelForm(forms.ModelForm):
	class Meta:
		model  = DocumentoIdentificacion
		fields = ['nombre']
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'Input-Text'}),
        }