# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.SlugField(default='default-slug'),
            preserve_default=False,
        ),
    ]
