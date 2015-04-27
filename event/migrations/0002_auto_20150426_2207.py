# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='address',
            field=models.CharField(max_length=245, blank=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='cell_phone',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='city',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='first_name',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='home_phone',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='last_name',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='state',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='zipcode',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
