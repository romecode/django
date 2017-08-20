# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupexpiration',
            name='profileid',
            field=models.CharField(max_length=14, verbose_name='Recurring ID', blank=True),
        ),
        migrations.AddField(
            model_name='groupexpiration',
            name='users',
            field=models.ManyToManyField(related_name='corporate_set', verbose_name='Additional Users', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='userexpiration',
            name='profileid',
            field=models.CharField(max_length=14, verbose_name='Recurring ID', blank=True),
        ),
    ]
