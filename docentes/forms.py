# -*- encoding: utf-8 -*-
from django import forms
from .models import Docente
from django.forms.formsets import formset_factory


class DocenteModelForm(forms.ModelForm):
	class Meta:
		model  = Docente
		fields = [
					'apellido_paterno','apellido_materno', 'nombre', 'documento_identificacion',
					'numero_documento_identificacion', 'fecha_nacimiento', 'genero', 'estado_civil', 'grupo_sanguineo','fotografia',
					'hijo', 'numero_hijo',
					'observacion_persona', 'distrito', 'zona', 'via', 'nombre_direccion', 'edificio','departamento', 'apartamento', 'bloque', 
					'pabellon','piso', 'interior', 'pasadizo', 'numero',
					'cuadra', 'manzana', 'etapa', 'lote','sub_lote', 'sector', 'kilometro','denominacion', 'referencia', 'observacion_direccion',
					'telefono_personal', 'celular_personal','email_personal', 'idioma',

					'entidad',
					'usuario', 'cargo', 'grado_instruccion', 'profesion', 'ocupacion', 
				 	'email_corporativo', 'fecha_inicio_contratacion',
				 	'fecha_inicio_contratacion', 'fecha_fin_contratacion', 'fecha_cese',
				 	'tipo_docente',
		         ]

		widgets = {
				'apellido_paterno'			     : forms.TextInput(attrs={'class':'InputText'}),
				'apellido_materno'			     : forms.TextInput(attrs={'class':'InputText'}),
				'nombre'		  			     : forms.TextInput(attrs={'class':'InputText'}),
				'documento_identificacion'	     : forms.Select(attrs={'class':'Select'}),
				'numero_documento_identificacion': forms.TextInput(attrs={'class':'InputText'}),
				'fecha_nacimiento'			     : forms.DateInput(attrs={'type':'date', 'class':'InputDate', 'value':'01/01/1980'}),

				'genero' 						 : forms.RadioSelect(attrs={'class':'RadioButton'}),
				'estado_civil' 					 : forms.Select(attrs={'class':'Select'}),
				'grupo_sanguineo'				 : forms.Select(attrs={'class':'Select'}),
				'fotografia'  					 : forms.FileInput(attrs={'class':'InputFile'}),

				'hijo' 							 : forms.RadioSelect(attrs={'class':'RadioButton'}),
				'numero_hijo'					 : forms.NumberInput(attrs={'class':'InputText'}),

				'observacion_persona'			 : forms.Textarea(attrs={'class':'InputArea', }),
				'distrito' 						 : forms.Select(attrs={'class':'Select'}),
				'zona'							 : forms.Select(attrs={'class':'Select'}),
				'via'							 : forms.Select(attrs={'class':'Select'}),
				'nombre_direccion'				 : forms.TextInput(attrs={'class':'InputText'}),
				'edificio'						 : forms.TextInput(attrs={'class':'InputText'}),
				'apartamento'					 : forms.TextInput(attrs={'class':'InputText'}),
				'departamento'					 : forms.TextInput(attrs={'class':'InputText'}),
				'pabellon'					 	 : forms.TextInput(attrs={'class':'InputText'}),
				'bloque'					 	 : forms.TextInput(attrs={'class':'InputText'}),
				'piso'							 : forms.TextInput(attrs={'class':'InputText'}),
				'interior'						 : forms.TextInput(attrs={'class':'InputText'}),
				'pasadizo'						 : forms.TextInput(attrs={'class':'InputText'}),
				'numero' 						 : forms.TextInput(attrs={'class':'InputText'}),
				'cuadra'						 : forms.TextInput(attrs={'class':'InputText'}),
				'manzana'						 : forms.TextInput(attrs={'class':'InputText'}),
				'etapa'							 : forms.TextInput(attrs={'class':'InputText'}),
				'lote'							 : forms.TextInput(attrs={'class':'InputText'}),
				'sub_lote'						 : forms.TextInput(attrs={'class':'InputText'}),
				'sector'						 : forms.TextInput(attrs={'class':'InputText'}),
				'kilometro'						 : forms.TextInput(attrs={'class':'InputText'}),
				'denominacion'					 : forms.Textarea(attrs={'class':'InputArea'}),
				'referencia'					 : forms.Textarea(attrs={'class':'InputArea'}),
				'observacion_direccion'			 : forms.Textarea(attrs={'class':'InputArea', }),
				'telefono_personal'				 : forms.TextInput(attrs={'class':'InputText'}), 
				'celular_personal'				 : forms.TextInput(attrs={'class':'InputText'}), 
				'email_personal'				 : forms.EmailInput(attrs={'class':'InputText', 'placeholder':'example@example.com'}),

				'entidad'						: forms.Select(attrs={'class':'Select'}),
				'usuario'	  	   	 			: forms.Select(attrs={'class':'Select'}),
				'tipo_docente'  				: forms.Select(attrs={'class':'Select'}),
	            'cargo'  						: forms.Select(attrs={'class':'Select'}),
	            'grado_instruccion'  			: forms.Select(attrs={'class':'Select'}),
	            'profesion'  					: forms.Select(attrs={'class':'Select'}),
	            'ocupacion'  					: forms.Select(attrs={'class':'Select'}),
	          	'idioma'  						: forms.Select(attrs={'class':'Select'}),
	            'email_corporativo'  			: forms.EmailInput(attrs={'class':'InputText', 'placeholder':'example@example.com'}),
	            'fecha_inicio_contratacion' 	: forms.DateInput(attrs={'type':'date', 'class':'InputDate'}),
	            'fecha_fin_contratacion'  		: forms.DateInput(attrs={'type':'date', 'class':'InputDate'}),
	            'fecha_cese'  					: forms.DateInput(attrs={'type':'date', 'class':'InputDate'}),
             }



