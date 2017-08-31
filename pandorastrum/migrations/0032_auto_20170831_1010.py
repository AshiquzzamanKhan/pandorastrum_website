# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandorastrum', '0031_auto_20170831_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamegenre',
            name='game_genre',
            field=models.CharField(choices=[('INFINITE RUNNER', 'Infinite Runner'), ('RPG', 'Rpg'), ('2D', '2D'), ('3D', '3d'), ('MOBA', 'Moba'), ('SPORTS', 'Sports'), ('SIMULATION', 'Simulation'), ('STRATEGY', 'Strategy'), ('TRIVIA', 'Trivia'), ('3RD PERSON', '3rd Person'), ('SPACE', 'Space'), ('MMO', 'Mmo'), ('PUZZLE', 'Puzzle'), ('PLATFORMER', 'Platformer'), ('HACK N SLASH', 'Hack n slash'), ('BEAT EM UP', 'Beat em up'), ('SHOOTING', 'Shooting'), ('ACTION', 'Action'), ('ADVENTURE', 'Adventure'), ('FPS', 'Fps'), ('ARCADE', 'Arcade'), ('RACING', 'Racing'), ('---', '---')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='gamesmodel',
            name='game_short_description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='portfoliomodel',
            name='category_type',
            field=models.CharField(choices=[('CONCEPT', 'Concept'), ('UNITY', 'Unity'), ('3D', '3d'), ('UNREAL', 'Unreal'), ('EXPERIMENTAL', 'Experimental')], max_length=12),
        ),
    ]
