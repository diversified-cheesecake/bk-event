# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20150426_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='email',
            field=models.CharField(max_length=245, blank=True),
        ),
    ]
