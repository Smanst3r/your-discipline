# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-14 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_auto_20181108_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='discipline',
            name='about',
            field=models.TextField(default="Опис дисципліни. Наприклад Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. ", max_length=500),
        ),
    ]
