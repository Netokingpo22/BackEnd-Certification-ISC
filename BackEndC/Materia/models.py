from django.db import models

from Carrera.models import Carrera
from Maestro.models import Maestro

# Create your models here.

class IntencionDidactica(models.Model):
    nombre = models.CharField(max_length=512)


tipoMaterias = {
    'O': 'Especialidad',
    'C': 'Comun',
}

class Materia(models.Model):
    carerra = models.ForeignKey(Carrera, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=256)
    clave = models.CharField(max_length=32, null=False)
    creditosTeoricos = models.IntegerField()
    creditosPracticos = models.IntegerField()
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT)
    competenciaGeneral = models.TextField()
    intencionDidactica = models.ForeignKey(IntencionDidactica, on_delete=models.PROTECT)
    caracterizacion = models.TextField()
    tipoMateria = models.CharField(max_length=32, choices=tipoMaterias.items())
    semestre = models.IntegerField()
