# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Img(models.Model):
    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
    name = models.CharField(max_length=255, default="undefined", verbose_name="Nom")
    file = models.ImageField(upload_to='upload', verbose_name="Fichier")

    def __str__(self):
        return self.name + ' - ' + self.style


