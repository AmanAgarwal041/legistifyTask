# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='fname',
            field=models.CharField(default='Test', max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='login',
            name='uname',
            field=models.EmailField(unique=True, max_length=120),
        ),
    ]
