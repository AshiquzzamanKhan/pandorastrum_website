# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 21:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pandorastrum', '0023_auto_20170816_0334'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamesDev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=400, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('completion_date', models.DateField(blank=True, null=True)),
                ('related_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pandorastrum.GamesModel')),
            ],
        ),
    ]