# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Image(models.Model):
    CHOICES = (
        ("ORIGINAL", "ORIGINAL"),
        ("RED", "RED"),
        ("BLUE", "BLUE"),
        ("GREEN", "GREEN"),
        ("NEGATIVE", "NEGATIVE"),
        ("BLACK&WHITE", "BLACK&WHITE")
    )
    name = models.CharField(max_length=255, default="undefined"),
    path = models.CharField(max_length=255, default="/img"),
    style = models.CharField(max_length=255, choices=CHOICES, default="ORIGINAL")


