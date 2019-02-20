# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-04 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_model', '0006_auto_20190201_2041'),
        ('cart', '0005_auto_20190203_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='user_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='user_model.register_model'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carttotal',
            name='user_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='user_model.register_model'),
            preserve_default=False,
        ),
    ]