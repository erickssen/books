# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-20 23:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('shipping_name', models.CharField(max_length=50)),
                ('shipping_address_1', models.CharField(max_length=50)),
                ('shipping_address_2', models.CharField(blank=True, max_length=50)),
                ('shipping_city', models.CharField(max_length=50)),
                ('shipping_state', models.CharField(max_length=2)),
                ('shipping_zip', models.CharField(max_length=10)),
                ('shipping_country', models.CharField(max_length=50)),
                ('billing_name', models.CharField(max_length=50)),
                ('billing_address_1', models.CharField(max_length=50)),
                ('billing_address_2', models.CharField(blank=True, max_length=50)),
                ('billing_city', models.CharField(max_length=50)),
                ('billing_state', models.CharField(max_length=2)),
                ('billing_zip', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
