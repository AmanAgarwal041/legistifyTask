# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20160226_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactlawyer',
            name='id',
        ),
        migrations.AddField(
            model_name='contactlawyer',
            name='contact_id',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
