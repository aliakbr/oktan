# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 15:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oktansite', '0010_timeline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timeline',
            old_name='title',
            new_name='tanggal',
        ),
    ]
