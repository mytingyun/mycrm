# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-19 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostManage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=64, verbose_name='主机名')),
                ('servername', models.CharField(max_length=32, verbose_name='服务功能')),
            ],
        ),
    ]