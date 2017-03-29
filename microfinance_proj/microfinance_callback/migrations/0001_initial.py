# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-28 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Microfinance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phonenumber', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=30)),
                ('validation', models.CharField(max_length=30)),
                ('reg_date', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='session_levels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=60)),
                ('phonenumber', models.CharField(max_length=25)),
                ('level', models.IntegerField()),
            ],
        ),
    ]
