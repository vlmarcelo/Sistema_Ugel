# -*- encoding: utf-8 -*-
from django import forms
from .models import Cargo


class CargoModelForm(forms.ModelForm):
	class Meta:
		model  = Cargo
		fields = ['nombre']
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'Input-Text'}),
        }