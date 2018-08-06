# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-05 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('billing_number', models.BigIntegerField(primary_key=True, serialize=False)),
                ('customer', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('purchase_date', models.DateTimeField()),
                ('company', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('serial_number', models.BigIntegerField()),
                ('mfg_date', models.DateTimeField()),
                ('shipping_date', models.DateTimeField()),
            ],
        ),
    ]