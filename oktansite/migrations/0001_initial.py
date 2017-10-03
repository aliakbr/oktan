# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 08:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import oktansite.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('email_confirmed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MediaPartner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('src', models.ImageField(upload_to=oktansite.models.get_upload_path_images_media_partner)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('src', models.ImageField(upload_to=oktansite.models.get_upload_path_images_gallery)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('src', models.ImageField(upload_to=oktansite.models.get_upload_path_images_sponsor)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('team_name', models.CharField(max_length=50, unique=True)),
                ('supervisor_name', models.CharField(max_length=100)),
                ('school_name', models.CharField(max_length=150)),
                ('proof_of_payment', models.FileField(upload_to=oktansite.models.get_upload_path_images_payment)),
                ('student_name_1', models.CharField(max_length=100, null=True)),
                ('student_phone_number_1', models.CharField(max_length=50, null=True)),
                ('student_id_number_1', models.CharField(max_length=100, null=True)),
                ('student_card_image_1', models.ImageField(null=True, upload_to=oktansite.models.get_upload_path_images_student_card1)),
                ('student_name_2', models.CharField(max_length=100, null=True)),
                ('student_phone_number_2', models.CharField(max_length=50, null=True)),
                ('student_id_number_2', models.CharField(max_length=100, null=True)),
                ('student_card_image_2', models.ImageField(null=True, upload_to=oktansite.models.get_upload_path_images_student_card2)),
                ('proof_code', models.CharField(max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tanggal', models.CharField(max_length=120)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='team',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='oktansite.Team'),
        ),
    ]