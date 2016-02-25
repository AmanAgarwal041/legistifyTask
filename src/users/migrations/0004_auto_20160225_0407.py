# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160225_0342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lawyerdetail',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='fname',
        ),
        migrations.AddField(
            model_name='lawyerdetail',
            name='age',
            field=models.IntegerField(default=23, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lawyerdetail',
            name='experience',
            field=models.IntegerField(default=4, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lawyerdetail',
            name='gen',
            field=models.CharField(default='M', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='age',
            field=models.IntegerField(default=25, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='gen',
            field=models.CharField(default='F', max_length=1),
            preserve_default=False,
        ),
    ]
