from django.db import models
from simple_history.models import HistoricalRecords

#Modelo para autores
class Autor(models.Model):
    nombre =models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    fecha_nacimiento =models.DateField()
    nacionalidad =models.CharField(max_length=100)
    biografia = models.TextField()
    email=models.EmailField()
    telefono =models.CharField(max_length=20)
    sitio_web= models.URLField()
    premios = models.TextField()
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
