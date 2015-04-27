# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20150427_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='showed_up',
            field=models.BooleanField(default=True),
        ),
    ]
