# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-12 05:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tipos_personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipopersona',
            name='ultimo_usuario_editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipo_persona_usuario_editor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tipopersona',
            name='usuario_creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
