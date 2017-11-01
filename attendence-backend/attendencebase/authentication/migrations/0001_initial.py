# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-31 06:06
from __future__ import unicode_literals

import authentication.models.user
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_on', models.DateTimeField(null=True)),
                ('updated_on', models.DateTimeField(null=True)),
                ('username', models.CharField(max_length=60, null=True)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile_number', models.CharField(default=None, max_length=13, null=True, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\d{10}$')])),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('avatar_url', models.URLField(blank=True, max_length=300, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1, null=True)),
                ('age', models.IntegerField(blank=True, default=10, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            managers=[
                ('objects', authentication.models.user.UserManager()),
            ],
        ),
    ]