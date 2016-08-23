# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-16 05:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuestionarios', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('docentes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuestionario',
            name='docente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='docentes.Docente'),
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='ultimo_usuario_editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuestionario_usuario_editor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='usuario_creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]