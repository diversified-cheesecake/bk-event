# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_attendee_input_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='showed_up',
            field=models.BooleanField(default=False),
        ),
    ]
