# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oktansite', '0009_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('text', models.TextField()),
            ],
        ),
    ]
