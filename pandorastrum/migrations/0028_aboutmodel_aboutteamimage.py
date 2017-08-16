# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 00:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pandorastrum', '0027_auto_20170816_0401'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generic_model', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AboutTeamImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('img', models.ImageField(blank=True, null=True, upload_to='about')),
                ('fb_url', models.URLField(default='')),
                ('tw_url', models.URLField(default='')),
                ('post_title', models.CharField(blank=True, max_length=100, null=True)),
                ('related_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pandorastrum.AboutModel')),
            ],
        ),
    ]