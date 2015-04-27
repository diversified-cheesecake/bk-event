# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_attendance_showed_up'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='showed_up',
            field=models.BooleanField(),
        ),
    ]
