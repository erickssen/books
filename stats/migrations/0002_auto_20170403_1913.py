# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-03 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productview',
            name='tracking_id',
            field=models.CharField(db_index=True, default='', max_length=50),
        ),
    ]
