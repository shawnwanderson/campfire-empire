# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-22 23:21
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0002_auto_20161217_0231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', django_markdown.models.MarkdownField(blank=True)),
                ('artists', models.ManyToManyField(to='artists.Artist')),
            ],
        ),
    ]