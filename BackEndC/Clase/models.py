from django.db import models

from Maestro.models import Maestro
from Materia.models import Materia
from Tema.models import Tema

# Create your models here.

class Aula(models.Model):
    nombre = models.TextField()

semestres = {
    '1': 'Enero-Mayo',
    '2': 'Verano',
    '3': 'Agosto-Diciembre',
}

class Grupo (models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT)
    numero = models.IntegerField()
    año = models.IntegerField()
    semestre = models.CharField(max_length=32, choices=semestres.items())

class Clase(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT)
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT)
    aula = models.ForeignKey(Aula, on_delete=models.PROTECT)
