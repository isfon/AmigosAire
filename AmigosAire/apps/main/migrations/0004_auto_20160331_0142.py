# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 01:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_datosgenerales_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicios',
            old_name='Descripcion',
            new_name='descripcion',
        ),
    ]
