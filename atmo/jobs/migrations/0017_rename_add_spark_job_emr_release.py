# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-21 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clusters', '0020_emr_release_model'),
        ('jobs', '0016_auto_20170320_0943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sparkjob',
            old_name='emr_release',
            new_name='emr_release_version',
        ),
        migrations.AddField(
            model_name='sparkjob',
            name='emr_release',
            field=models.ForeignKey(blank=True, help_text='Different AWS EMR versions have different versions of software like Hadoop, Spark, etc. See <a href="http://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-whatsnew.html">what\'s new</a> in each.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_sparkjobs', to='clusters.EMRRelease', verbose_name='EMR release'),
        ),
    ]
