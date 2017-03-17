# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0029_merge_20170316_0302'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CurriculumLink',
            new_name='CurriculumArea',
        ),
        migrations.RemoveField(
            model_name='followupactivity',
            name='curriculum_links',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='curriculum_links',
        ),
        migrations.AddField(
            model_name='followupactivity',
            name='curriculum_areas',
            field=models.ManyToManyField(related_name='follow_up_activity_curriculum_areas', to='topics.CurriculumArea'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='curriculum_areas',
            field=models.ManyToManyField(related_name='lesson_curriculum_areas', to='topics.CurriculumArea'),
        ),
    ]