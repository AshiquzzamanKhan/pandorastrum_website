# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandorastrum', '0009_auto_20170821_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='blog_banner',
            field=models.ImageField(blank=True, null=True, upload_to='blogs'),
        ),
    ]