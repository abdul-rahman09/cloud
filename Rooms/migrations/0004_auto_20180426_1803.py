# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-26 18:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rooms', '0003_auto_20180426_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='userid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='User.User'),
        ),
    ]
