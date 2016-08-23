# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-17 06:44
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienciaTrabajoAula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Escribir experiencia trabajo aula.', max_length=255, unique=True)),
                ('puntaje', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('nombre_host', models.CharField(max_length=255)),
                ('direccion_ip', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address])),
                ('ultimo_usuario_editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experienciatrabajoaula_usuario_editor', to=settings.AUTH_USER_MODEL)),
                ('usuario_creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('nombre',),
                'db_table': 'Experiencias_Trabajos_Aulas',
                'verbose_name': 'Experiencia_Trabajo_Aula',
                'verbose_name_plural': 'Experiencias_Trabajos_Aulas',
            },
        ),
    ]
