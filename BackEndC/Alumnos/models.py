from django.db import models

# Create your models here.

generos = {
    'M': 'Masculino',
    'F': 'Femenino',
    'N': 'No binario',
}

class Alumnos(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    matricula = models.CharField(max_length=16)
    genero = models.CharField(max_length=32, choices=generos.items())