# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20150426_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='my_campaign_id',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
