# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-30 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mi', '0007_auto_20161130_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='sector_team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='hvcs', to='mi.SectorTeam'),
            preserve_default=False,
        ),
    ]
