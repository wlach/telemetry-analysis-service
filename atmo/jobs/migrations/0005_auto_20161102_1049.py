# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-02 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_sparkjob_emr_release'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparkjob',
            name='most_recent_status',
            field=models.CharField(blank=True, default=b'', max_length=50),
        ),
    ]