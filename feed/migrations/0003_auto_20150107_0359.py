# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20150106_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='member',
            field=models.ManyToManyField(related_name='subscriber', null=True, to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
