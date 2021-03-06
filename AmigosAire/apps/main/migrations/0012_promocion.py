# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20160416_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='servicios')),
                ('promocion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Promociones',
                'verbose_name': 'Promocion',
            },
        ),
    ]
