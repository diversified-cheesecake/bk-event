# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_attendee_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='showed_up',
        ),
        migrations.AddField(
            model_name='attendance',
            name='input_by',
            field=models.CharField(max_length=245, blank=True),
        ),
    ]
