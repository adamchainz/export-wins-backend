# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-04 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi', '0013_auto_20161130_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='target',
            field=models.BigIntegerField(),
        ),
    ]