# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba_news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500)),
                ('url_image', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
