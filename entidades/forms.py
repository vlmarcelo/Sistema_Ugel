# -*- encoding: utf-8 -*-
from django import forms
from .models import Entidad

from django.forms.formsets import formset_factory


class EntidadModelForm(forms.ModelForm):

	class Meta:
		model  = Entidad
		fields = [
				  'clase_entidad', 'tipo_entidad', 'nombre','siglas', 'documento_identificacion', 
				  'numero_documento_identificacion', 'mision', 'vision', 
				  'fecha_creacion', 'fecha_cese', 'descripcion', 'observacion', 'logotipo', 'activo',
				 ]

		widgets = {
				'clase_entidad'			     	 : forms.Select(attrs={'class':'Select'}),
				'tipo_entidad'			    	 : forms.Select(attrs={'class':'Select'}),
				'nombre'		  			     : forms.TextInput(attrs={'class':'InputText'}),
				'siglas'	     				 : forms.TextInput(attrs={'class':'InputText'}),
				'documento_identificacion'		 : forms.Select(attrs={'class':'Select'}),
				'numero_documento_identificacion': forms.TextInput(attrs={'class':'InputText'}),
				'mision'						 : forms.Textarea(attrs={'class':'InputArea'}),
				'vision'  						 : forms.Textarea(attrs={'class':'InputArea'}),
				'logotipo'						 : forms.FileInput(attrs={'class':'InputFile'}),
				'fecha_creacion' 				 : forms.DateInput(attrs={'class':'InputDate'}),
				'fecha_cese'					 : forms.DateInput(attrs={'class':'InputDate'}),
				'descripcion'					 : forms.Textarea(attrs={'class':'InputArea', }),
				'observacion' 					 : forms.Textarea(attrs={'class':'InputArea', }),
				'activo'						 : forms.CheckboxInput(attrs={'class':'Checkbox', })
             }



