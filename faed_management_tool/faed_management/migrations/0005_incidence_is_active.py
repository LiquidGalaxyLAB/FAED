# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faed_management', '0004_remove_incidence_drone'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidence',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]