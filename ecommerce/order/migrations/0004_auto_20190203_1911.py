# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-03 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20190203_0740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_total',
        ),
        migrations.AddField(
            model_name='order_total',
            name='order_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='order.Order'),
            preserve_default=False,
        ),
    ]
