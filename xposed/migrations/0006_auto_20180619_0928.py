# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-19 09:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xposed', '0005_auto_20180619_0919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='xposed_models',
            old_name='verification',
            new_name='is_model',
        ),
    ]
