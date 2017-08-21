# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandorastrum', '0008_auto_20170819_2214'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogmodel',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveField(
            model_name='blogmodel',
            name='blog_thumbnail',
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]