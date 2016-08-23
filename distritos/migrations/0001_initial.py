# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-12 05:01
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Escribir nombre del distrito.', max_length=255, unique=True)),
                ('imagen', models.ImageField(blank=True, default='default/No-Image-1.png', help_text='Subir imagen de la distrito. (Opcional)', upload_to='imagenes_distritos')),
                ('descripcion', models.TextField(blank=True, help_text='Escribir descripci\xf3n de la distrito. (Opcional)')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('nombre_host', models.CharField(max_length=255)),
                ('direccion_ip', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address])),
            ],
            options={
                'ordering': ('nombre',),
                'db_table': 'Distritos',
                'verbose_name': 'Distrito',
                'verbose_name_plural': 'Distritos',
            },
        ),
    ]
