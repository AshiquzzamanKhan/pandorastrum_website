# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandorastrum', '0010_blogmodel_blog_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcontentmodel',
            name='attach_banner_here',
            field=models.BooleanField(default=False),
        ),
    ]
