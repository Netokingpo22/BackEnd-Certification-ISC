from django.db import models

class IntencionDidactica(models.Model):
    nombre = models.CharField(max_length=512)