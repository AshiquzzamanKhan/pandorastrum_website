# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pandorastrum', '0005_auto_20170826_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_genre', models.CharField(choices=[('MMO', 'Mmo'), ('PUZZLE', 'Puzzle'), ('FPS', 'Fps'), ('TRIVIA', 'Trivia'), ('---', '---'), ('SIMULATION', 'Simulation'), ('STRATEGY', 'Strategy'), ('2D', '2D'), ('SPORTS', 'Sports'), ('3D', '3d'), ('HACK N SLASH', 'Hack n slash'), ('3RD PERSON', '3rd Person'), ('PLATFORMER', 'Platformer'), ('RPG', 'Rpg'), ('SPACE', 'Space'), ('INFINITE RUNNER', 'Infinite Runner'), ('ADVENTURE', 'Adventure'), ('MOBA', 'Moba'), ('ACTION', 'Action'), ('BEAT EM UP', 'Beat em up'), ('ARCADE', 'Arcade'), ('SHOOTING', 'Shooting'), ('RACING', 'Racing')], default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GameLore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_title', models.CharField(blank=True, max_length=200, null=True)),
                ('topic', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='GamesDev',
            new_name='GamesTimeline',
        ),
        migrations.RenameModel(
            old_name='GameRequirements',
            new_name='SystemRequirements',
        ),
        migrations.AddField(
            model_name='gamesdownloadlink',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gamesgallery',
            name='img_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='gamesmodel',
            name='age_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='portfoliomodel',
            name='category_type',
            field=models.CharField(choices=[('CONCEPT', 'Concept'), ('EXPERIMENTAL', 'Experimental'), ('UNREAL', 'Unreal'), ('UNITY', 'Unity'), ('3D', '3d')], max_length=12),
        ),
        migrations.AddField(
            model_name='gamelore',
            name='related_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pandorastrum.GamesModel'),
        ),
        migrations.AddField(
            model_name='gamegenre',
            name='related_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pandorastrum.GamesModel'),
        ),
    ]