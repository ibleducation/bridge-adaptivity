# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-14 14:14
from __future__ import unicode_literals

from django.db import migrations, models


def set_order_values(apps, schema_editor):
    Activity = apps.get_model('module', 'Activity')
    for activity in Activity.objects.all().iterator():
        activity.order = activity.id
        activity.save()


class Migration(migrations.Migration):
    dependencies = [
        ('module', '0011_auto_20170914_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='atype',
            field=models.CharField(
                choices=[(b'g', 'generic'), (b's', 'pre-assessment'), (b'f', 'post-assessment')],
                default=b'g', max_length=1
            ),
        ),
        migrations.AddField(
            model_name='activity',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
            preserve_default=False,
        ),
        # NOTE(wowkalucky): set order values manually to id value
        migrations.RunPython(set_order_values),
    ]
