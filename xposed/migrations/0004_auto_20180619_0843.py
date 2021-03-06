# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-19 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xposed', '0003_auto_20180614_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='xposed_models',
            name='weight',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='xposed_models',
            name='bust',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='xposed_models',
            name='height',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='xposed_models',
            name='hips',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='xposed_models',
            name='shoes_size',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='xposed_models',
            name='verification',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='xposed_models',
            name='waist',
            field=models.SmallIntegerField(),
        ),
    ]
