# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-23 15:52
from __future__ import unicode_literals

from django.db import migrations


def update(apps, schema_editor):
    Win = apps.get_model('wins', 'Win')
    Advisor = apps.get_model('wins', 'Advisor')
    to_remove = [
        'itt:DIT South West (Northern Zone)',
        'itt:DIT South West (Southern Zone)',
    ]
    for Kls in [Win, Advisor]:
        for remove_team in to_remove:
            for obj in Kls.objects.filter(hq_team=remove_team):
                print('fixing', obj, obj.hq_team)
                obj.hq_team = 'itt:DIT South West'
                obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('wins', '0024_auto_20160905_1046'),
    ]

    operations = [
        migrations.RunPython(update),
    ]