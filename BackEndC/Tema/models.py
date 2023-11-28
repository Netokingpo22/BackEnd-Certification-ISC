from django.db import models

# Create your models here.


class ActividadEnseñanza(models.Model):
    nombre = models.TextField()


class ActividadAprendizaje(models.Model):
    nombre = models.TextField()


class CompetenciaGenerica(models.Model):
    nombre = models.TextField()


class InstrumentoEvaluacion(models.Model):
    nombre = models.TextField()
    URL = models.TextField()


class Tema(models.Model):
    nombre = models.TextField()
    actividadEnseñanza = models.ForeignKey(
        ActividadEnseñanza, on_delete=models.PROTECT)
    actividadAprendizaje = models.ForeignKey(
        ActividadAprendizaje, on_delete=models.PROTECT)
    horasTeoria = models.IntegerField()
    horasPractica = models.IntegerField()
    competenciaGenerica = models.ForeignKey(
        CompetenciaGenerica, on_delete=models.PROTECT)
    portafolioEvidencia = models.BooleanField(default=False)
    instrumentoEvaluacion = models.ForeignKey(
        InstrumentoEvaluacion, on_delete=models.PROTECT)
