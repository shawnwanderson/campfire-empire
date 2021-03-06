# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-22 23:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(blank=True, null=True, verbose_name='Time'),
        ),
    ]
