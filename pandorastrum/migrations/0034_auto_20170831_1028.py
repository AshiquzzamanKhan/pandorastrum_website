# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandorastrum', '0033_auto_20170831_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamegenre',
            name='game_genre',
            field=models.CharField(choices=[('Trivia', 'Trivia'), ('Action', 'Action'), ('Arcade', 'Arcade'), ('3d', '3d'), ('Puzzle', 'Puzzle'), ('Adventure', 'Adventure'), ('Racing', 'Racing'), ('MOBA', 'MOBA'), ('3rd Person', '3rd Person'), ('Beat-em-up', 'Beat-em-up'), ('Shooting', 'Shooting'), ('Driving', 'Driving'), ('FPS', 'FPS'), ('Strategy', 'Strategy'), ('Platformer', 'Platformer'), ('---', '---'), ('Sports', 'Sports'), ('Simulation', 'Simulation'), ('RPG', 'RPG'), ('Hack N Slash', 'Hack N Slash'), ('Space', 'Space'), ('MMO', 'MMO'), ('Infinite Runner', 'Infinite Runner'), ('2d', '2d')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='gamelore',
            name='topic_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='gamestimeline',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='gamestimeline',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='portfoliomodel',
            name='category_type',
            field=models.CharField(choices=[('3D', '3d'), ('EXPERIMENTAL', 'Experimental'), ('UNREAL', 'Unreal'), ('CONCEPT', 'Concept'), ('UNITY', 'Unity')], max_length=12),
        ),
        migrations.AlterField(
            model_name='upcominggamesmodel',
            name='code_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='upcominggamesmodel',
            name='game_teaser_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]