from django.db import models

# Create your models here.

class Carrera(models.Model):
    nombre = models.CharField(max_length=256)
    siglas = models.CharField(max_length=16)
