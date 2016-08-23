# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario
from .forms import UsuarioModelForm 

@admin.register(Usuario)
# Por defecto el admin usa -> UserAdmin
class UsuarioAdmin(UserAdmin):
	
	list_display = ('username', 'email', 'password', 'avatar', 'slug', 'last_login', 'nombre_host', 'direccion_ip', 'is_staff', 'is_active')
	

	fieldsets = (
			('Usuario', {'fields':('username', 'password', 'email', 'avatar')}),

			('Permissions', {'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),

			('Info Sistema', {'fields':('nombre_host', 'direccion_ip')})
		)

	search_fields  = ('username', 'id')

	class Meta:
		model = Usuario 
		form_class = UsuarioModelForm