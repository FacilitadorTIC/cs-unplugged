# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-08 01:57
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0092_auto_20181105_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='agegroup',
            name='description_mi',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='classroomresource',
            name='description_mi',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='curriculumarea',
            name='name_mi',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='curriculumintegration',
            name='content_mi',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='curriculumintegration',
            name='name_mi',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='glossaryterm',
            name='definition_mi',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='glossaryterm',
            name='term_mi',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='learningoutcome',
            name='text_mi',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='computational_thinking_links_mi',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='content_mi',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='heading_tree_mi',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=list, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='name_mi',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='programming_challenges_description_mi',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='programmingchallenge',
            name='content_mi',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='programmingchallenge',
            name='extra_challenge_mi',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='programmingchallenge',
            name='name_mi',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='programmingchallengedifficulty',
            name='name_mi',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='programmingchallengeimplementation',
            name='expected_result_mi',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='programmingchallengeimplementation',
            name='hints_mi',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='programmingchallengeimplementation',
            name='solution_mi',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='programmingchallengelanguage',
            name='name_mi',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='resourcedescription',
            name='description_mi',
            field=models.CharField(default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='content_mi',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='name_mi',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='other_resources_mi',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='unitplan',
            name='computational_thinking_links_mi',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='unitplan',
            name='content_mi',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='unitplan',
            name='heading_tree_mi',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, null=True),
        ),
        migrations.AddField(
            model_name='unitplan',
            name='name_mi',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]