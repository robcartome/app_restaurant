from django.db import models

# Create your models here.
class Platos(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=3, decimal_places=2)
    procedencia = models.CharField(max_length=40, default='')

    def __str__(self):
        return "Nombre: {}, Precio: {}".format(self.nombre, self.edad)
