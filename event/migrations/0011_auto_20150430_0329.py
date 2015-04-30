# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_attendee_showed_up'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='my_campaign_id',
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]
