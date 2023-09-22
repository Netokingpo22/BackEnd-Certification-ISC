from django.db import models

# Create your models here.

tiposEstudios = {
    'L': 'Licenciatura',
    'M': 'Maestria',
    'D': 'Doctorado',
    'P': 'Post Doctorado',
}

class Maestro(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    estudios = models.CharField(max_length=256)
    tipoEstudios = models.CharField(max_length=32, choices=tiposEstudios.items())
    fechaIngrso = models.DateField()
    puesto = models.CharField(max_length=256)