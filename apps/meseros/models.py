from django.db import models

# Create your models here.
class Meseros(models.Model):
    nombre = models.CharField(max_length=40)
    dni = models.CharField(max_length=8)
    procedencia = models.CharField(max_length=40, default='')
    edad = models.IntegerField(default=0)
