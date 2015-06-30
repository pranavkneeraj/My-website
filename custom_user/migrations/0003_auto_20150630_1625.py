# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0002_useractivationprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivationprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 6, 30)),
        ),
    ]
