# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-07 23:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oktansite', '0005_auto_20170907_0928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='student_id_card_1',
            new_name='student_id_number_1',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='student_id_card_2',
            new_name='student_id_number_2',
        ),
    ]