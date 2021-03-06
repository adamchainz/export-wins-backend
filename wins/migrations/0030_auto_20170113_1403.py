# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-13 14:03
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations


def do_thing(apps, schema_editor):
    """ Soft-delete relations of existing soft-deleted Wins """

    Win = apps.get_model('wins', 'Win')
    for win in Win.objects.filter(is_active=False):
        foreignkey_fields = [
            'advisors',
            'breakdowns',
            'notifications',
        ]
        for related_field in foreignkey_fields:
            related_objs = getattr(win, related_field).all()
            related_objs.update(is_active=False)

        # have to handle one-to-one differently
        try:
            confirmation = win.confirmation
        except ObjectDoesNotExist:
            pass
        else:
            confirmation.is_active = False
            confirmation.save()


class Migration(migrations.Migration):

    dependencies = [
        ('wins', '0029_auto_20170113_1402'),
    ]

    operations = [
        migrations.RunPython(do_thing),
    ]
