# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Car(models.Model):
    billing_number = models.BigIntegerField(primary_key=True)
    customer = models.CharField(max_length=100)
    price = models.IntegerField()
    purchase_date = models.DateField()
    company = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_number = models.BigIntegerField()
    mfg_date = models.DateField()
    shipping_date = models.DateField()
