# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-03 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loma', '0008_auto_20190203_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loma_attendance_model',
            name='loma_attendance',
            field=models.CharField(choices=[('A', 'Aa'), ('P', 'pp')], default='A', max_length=120),
        ),
    ]
