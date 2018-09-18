# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-27 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='ldap_name',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='nickname',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
