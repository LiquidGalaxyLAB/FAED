# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faed_management', '0005_incidence_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidence',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
