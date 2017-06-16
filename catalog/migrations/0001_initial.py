# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-20 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(help_text='Unique value for product page URL, created from name.', unique=True)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('meta_keywords', models.CharField(help_text='Content for description meta tag', max_length=255, verbose_name='Meta Keywords')),
                ('meta_description', models.CharField(default='meta description', help_text='context for description meta tag', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'categories',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(help_text='Unique value for product page URL, created from name.', max_length=255, unique=True)),
                ('brand', models.CharField(max_length=50)),
                ('sku', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9)),
                ('is_active', models.BooleanField(default=True)),
                ('is_bestseller', models.BooleanField(default=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('meta_keywords', models.CharField(help_text='Comma delimited set of SEO keywords for meta tag', max_length=255)),
                ('meta_description', models.CharField(help_text='Content for description meta tag', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, default='images/products/main', upload_to='images/products/main')),
                ('thumbnail', models.ImageField(blank=True, default='images/products/main', upload_to='images/products/thumbnails')),
                ('image_caption', models.CharField(blank=True, max_length=200)),
                ('categories', models.ManyToManyField(to='catalog.Category')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'products',
            },
        ),
    ]
