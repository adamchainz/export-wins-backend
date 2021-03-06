# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-30 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mi', '0005_auto_20161128_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('sector_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sectors', to='mi.SectorTeam')),
            ],
        ),
    ]
