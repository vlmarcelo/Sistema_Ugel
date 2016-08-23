# -*- encoding: utf-8 -*-
from django import forms
from .models import Via


class ViaModelForm(forms.ModelForm):
	class Meta:
		model  = Via
		fields = ['nombre']
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'Input-Text'}),
        }