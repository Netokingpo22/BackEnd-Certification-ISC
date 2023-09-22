from django.db import models

# Create your models here.

class Aula(models.Model):
    nombre = models.CharField(max_length=16)
