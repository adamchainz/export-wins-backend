# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-20 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mi', '0019_auto_20170119_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sector',
            name='parent_sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sectors', to='mi.ParentSector'),
        )
    ]
