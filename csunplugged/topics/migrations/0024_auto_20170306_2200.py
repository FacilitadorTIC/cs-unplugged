# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0023_programmingexerciselanguage_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programmingexerciselanguagesolution',
            name='slug',
        ),
        migrations.AddField(
            model_name='programmingexerciselanguagesolution',
            name='topic',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='solution', to='topics.Topic'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='programmingexerciselanguagesolution',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solution', to='topics.ProgrammingExercise'),
        ),
        migrations.AlterField(
            model_name='programmingexerciselanguagesolution',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solution', to='topics.ProgrammingExerciseLanguage'),
        ),
    ]
