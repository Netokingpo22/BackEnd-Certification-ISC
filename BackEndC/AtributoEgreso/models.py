from django.db import models

from Competencia.models import Competencia
from Tema.models import Tema

# Create your models here.

class Indicador(models.Model):
    competencia = models.ForeignKey(Competencia, on_delete=models.PROTECT)
    tema = models.ForeignKey(Tema, on_delete=models.PROTECT)

class CriterioDesempeño(models.Model):
    nombre = models.CharField(max_length=128)
    indicadores = models.ForeignKey(Indicador, on_delete=models.PROTECT)
    meta = models.TextField()

class AtributoEgreso(models.Model):
    criteriosDesempeño = models.ForeignKey(CriterioDesempeño, on_delete=models.PROTECT)
