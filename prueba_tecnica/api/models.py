from django.db import models
from datetime import date

# Create your models here.

class Producto(models.Model):
    categoria = models.CharField(max_length=30)
    descripcion = models.TextField()
    identificacion = models.CharField(max_length=10)
    fecha_inicio = models.DateField(default=date.today)
    nombre_producto = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.nombre_producto}, {self.categoria}, {self.valor}"