# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160225_0312'),
    ]

    operations = [
        migrations.CreateModel(
            name='LawyerDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lid', models.CharField(unique=True, max_length=120)),
                ('fname', models.CharField(max_length=120)),
                ('pno', models.IntegerField(max_length=12)),
                ('speciality', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.CharField(unique=True, max_length=120)),
                ('fname', models.CharField(max_length=120)),
                ('pno', models.IntegerField(max_length=12)),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]
