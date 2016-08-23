# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from django.core.validators import validate_ipv46_address
from django.template.defaultfilters import slugify
import socket
import os
from django.conf import settings


class UserManager(BaseUserManager):
	def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
		if not email:
			raise ValueError("El email es obligatorio")

		email = BaseUserManager.normalize_email(email)
		user  = self.model(username=username, email=email, is_active=True, is_staff=is_staff,is_superuser=is_superuser, **extra_fields)

		user.set_password(password)
		user.save(using=self._db)
		return user 

	def create_user(self, username, email, password, **extra_fields):
		try:
			extra_fields.setdefault('nombre_host', socket.gethostname())
		except:
		    extra_fields.setdefault('nombre_host', 'localhost')
		extra_fields.setdefault('direccion_ip', socket.gethostbyname(socket.gethostname()))

		return self._create_user(username, email,  password, True,True, **extra_fields)

	def create_superuser(self, username, email, password, **extra_fields):
		try:
			extra_fields.setdefault('nombre_host', socket.gethostname())
		except:
		    extra_fields.setdefault('nombre_host', 'localhost')
		extra_fields.setdefault('direccion_ip', socket.gethostbyname(socket.gethostname()))

		return self._create_user(username, email, password, True, True, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
	username 						= models.CharField(max_length=50, unique=True, db_index=True)	
	email    						= models.EmailField(max_length=50, unique=True)
	avatar   						= models.ImageField(blank=True, 
														null=True, 
														upload_to='avatar_usuario',
														default='default/No-Image-1.png',
														)
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True, db_index=True)
	fecha_registro 			   		= models.DateTimeField(auto_now_add=True, auto_now=False)
	#usuario_creador          	 	= models.ForeignKey('self')
	fecha_ultima_actualizacion 		= models.DateTimeField(auto_now_add=False, auto_now=True) 
	#ultimo_usuario_editor			= models.ForeignKey('self', related_name='usuario_usuario_editor')
	nombre_host				    	= models.CharField(max_length=255)
	direccion_ip			    	= models.GenericIPAddressField(validators=[validate_ipv46_address])
	
	objects = UserManager()

	is_active = models.BooleanField(default=True)
	is_staff  = models.BooleanField(default=True)

	USERNAME_FIELD  = 'username'
	REQUIRED_FIELDS = ['email']

	#Esto es cuando en la vista no existe un commit=false
	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.username)
		super(Usuario, self).save(*args, **kwargs)

	def get_short_name(self):
		return self.username
		
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Usuarios'
		#Ordenar los registros por un campo especifico
		ordering = ('id',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Usuario' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Usuarios'
