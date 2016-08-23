# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario


class UsuarioModelForm(forms.ModelForm):
	class Meta:
		model  = Usuario
		fields = ['username', 'email', 'password', 'avatar']
		widgets = {
			'username': forms.TextInput(attrs={'class':'InputText'}),
			'email'	  : forms.EmailInput(attrs={'class':'InputText', 'placeholder':'example@example.com'}),
            'password': forms.PasswordInput(attrs={'class':'InputText'}),
            'avatar'  : forms.FileInput(attrs={'class':'InputFile'}),
        }


class UsuarioAuthenticationForm(AuthenticationForm, forms.Form):
	username = forms.CharField(
	        max_length=255,
	        widget=forms.TextInput(attrs={
	        							  'autofocus'   : '',
	        							  'class'		: 'InputText', 
	        							  'placeholder' : 'Nombre de Usuario',	
	        							 }
	        					  ),
	    )
	password = forms.CharField(
			label=("Password"), 
			strip=False, 
			widget=forms.PasswordInput(attrs={'class': 'InputText', 'placeholder' : 'Password', })

			)
	
	class Meta:
		model = Usuario
		fields = '__all__'
		

class UserCreationEmailForm(UserCreationForm):
	email    = forms.EmailField()
	avatar	 = forms.ImageField()
	class Meta:
		model = Usuario 
		fields = ('username', 'email')