# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-21 12:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

CURRENT_EMR_RELEASES = (
    '5.2.1',
    '5.0.0',
)


def convert_emr_releases(apps, schema_editor):
    EMRRelease = apps.get_model('clusters', 'EMRRelease')
    Cluster = apps.get_model('clusters', 'Cluster')

    for cluster in Cluster.objects.all():
        emr_release, created = EMRRelease.objects.get_or_create(
            version=cluster.emr_release_version,
            defaults={
                'changelog_url': 'https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-%s/emr-release-components.html' % cluster.emr_release_version,
                'is_deprecated': cluster.emr_release_version not in CURRENT_EMR_RELEASES,
            }
        )
        cluster.emr_release = emr_release
        cluster.save()


def revert_emr_releases(apps, schema_editor):
    EMRRelease = apps.get_model('clusters', 'EMRRelease')
    Cluster = apps.get_model('clusters', 'Cluster')
    for cluster in Cluster.objects.all():
        cluster.emr_release = None
        cluster.save()


class Migration(migrations.Migration):

    dependencies = [
        ('clusters', '0020_emr_release_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cluster',
            old_name='emr_release',
            new_name='emr_release_version',
        ),
        migrations.AddField(
            model_name='cluster',
            name='emr_release',
            field=models.ForeignKey(blank=True, help_text='Different AWS EMR versions have different versions of software like Hadoop, Spark, etc. See <a href="http://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-whatsnew.html">what\'s new</a> in each.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_clusters', to='clusters.EMRRelease', verbose_name='EMR release'),
        ),
        migrations.RunPython(
            convert_emr_releases,
            revert_emr_releases,
        ),
        migrations.AlterField(
            model_name='cluster',
            name='emr_release',
            field=models.ForeignKey(help_text='Different AWS EMR versions have different versions of software like Hadoop, Spark, etc. See <a href="http://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-whatsnew.html">what\'s new</a> in each.', on_delete=django.db.models.deletion.PROTECT, related_name='created_clusters', to='clusters.EMRRelease', verbose_name='EMR release'),
        ),
        migrations.RemoveField(
            model_name='cluster',
            name='emr_release_version',
        ),
    ]
