# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160225_0407'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactLawyer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.CharField(unique=True, max_length=120)),
                ('lid', models.CharField(unique=True, max_length=120)),
                ('status', models.IntegerField(max_length=3)),
            ],
        ),
    ]
