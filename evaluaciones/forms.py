# -*- encoding: utf-8 -*-
from django import forms
from .models import Evaluacion


class EvaluacionModelForm(forms.ModelForm):
	class Meta:
		model  = Evaluacion
		fields = ['estudio_realizados', 'curso_capacitaion_pedagogico', 'formacion_capacitacion_aspecto_cargo',
				  'experiencia_sector_publico', 'experiencia_trabajo_aula', 'experiencia_docente', 
				  'experiencia_asesorias_acompanamientos', 'experiencia_procesos_capacitaciones_formacion']
		widgets = {
			#'pais'	: forms.ChoiceField(),
			'estudio_realizados': forms.Select(attrs={'class':'Select'}),
			'curso_capacitaion_pedagogico': forms.Select(attrs={'class':'Select'}),
	        'formacion_capacitacion_aspecto_cargo': forms.Select(attrs={'class':'Select'}),
            'experiencia_sector_publico' : forms.Select(attrs={'class':'Select'}),

            'experiencia_trabajo_aula'  : forms.Select(attrs={'class':'Select'}),
            'experiencia_docente' : forms.Select(attrs={'class':'Select'}),
            'experiencia_asesorias_acompanamientos'  : forms.Select(attrs={'class':'Select'}),
            'experiencia_procesos_capacitaciones_formacion' : forms.Select(attrs={'class':'Select'}),
        }

