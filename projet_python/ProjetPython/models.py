# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Image(models.Model):
    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
    CHOICES = (
        ("ORIGINAL", "ORIGINAL"),
        ("RED", "RED"),
        ("BLUE", "BLUE"),
        ("GREEN", "GREEN"),
        ("NEGATIVE", "NEGATIVE"),
        ("BLACK&WHITE", "BLACK&WHITE")
    )
    name = models.CharField(max_length=255, default="undefined", verbose_name="Nom")
    # path = models.CharField(max_length=255, default="/img", verbose_name="Chemin", unique=True)
    file = models.ImageField(upload_to='upload', verbose_name="Fichier")
    style = models.CharField(max_length=255, choices=CHOICES, default="ORIGINAL", verbose_name="Effet / Style")

    def __str__(self):
        return self.name + ' - ' + self.style


