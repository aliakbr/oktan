# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-06 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oktansite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
