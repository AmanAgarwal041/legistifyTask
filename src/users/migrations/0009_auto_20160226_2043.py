# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20160226_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactlawyer',
            name='lid',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='contactlawyer',
            name='uid',
            field=models.CharField(max_length=120),
        ),
    ]
