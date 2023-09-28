from django.db import models

from Clase.models import Clase
from Tema.models import Tema

# Create your models here.

generos = {
    'M': 'Masculino',
    'F': 'Femenino',
    'N': 'No binario',
}

class Alumno(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    matricula = models.CharField(max_length=16)
    genero = models.CharField(max_length=32, choices=generos.items())
    alumnoClase = models.ManyToManyField(Clase, through='AlumnoClase',related_name='alumnos_clases')
    alumnoTemaClase = models.ManyToManyField(Clase, through='AlumnoTemaClase', related_name='alumnos_temas_clases')

class AlumnoTemaClase(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT)
    tema = models.ForeignKey(Tema, on_delete=models.PROTECT)
    calificacion = models.IntegerField()
    evidencia = models.TextField()
    clase = models.ForeignKey(Clase, on_delete=models.PROTECT)

class AlumnoClase(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.PROTECT)
    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT)

