# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='input_by',
            field=models.CharField(max_length=245, blank=True),
        ),
    ]
