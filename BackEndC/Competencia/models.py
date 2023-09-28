from django.db import models

from Tema.models import Tema
from Materia.models import Materia

# Create your models here.

niveles = {
    'I': 'Introductorio',
    'M': 'Medio',
    'A': 'Avanzado',
}

class Competencia(models.Model):
    nombre = models.CharField(max_length=256)
    temas = models.ManyToManyField(Tema)
    nivel = models.CharField(max_length=32, choices=niveles.items())
    resumen = models.TextField()

tiposCompetencia = {
    '1': 'Ingreso',
    '2': 'Egreso',
}

class ListaCompetencia(models.Model):
    competencia = models.ForeignKey(Competencia, on_delete=models.PROTECT)
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT)
    tipoCompetencia = models.CharField(max_length=32, choices=tiposCompetencia.items())
