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

class Tema(models.Model):
    nombre = models.TextField()
    actividadEnseñanza = models.ManyToManyField(ActividadEnseñanza)
    actividadAprendizaje = models.ManyToManyField(ActividadAprendizaje)
    horasTeoria = models.IntegerField()
    horasPractica = models.IntegerField()
    competenciaGenerica = models.ManyToManyField(CompetenciaGenerica)
    portafolioEvidencia = models.BooleanField(default=False)
    instrumentoEvaluacion = models.ForeignKey(InstrumentoEvaluacion, on_delete=models.PROTECT)
