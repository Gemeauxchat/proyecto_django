from django.db import models
from simple_history.models import HistoricalRecords

#Modelo par editoriales
class Editorial(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais= models.CharField(max_length=100)
    codigo_postal =models.CharField(max_length=20)
    telefono =models.CharField(max_length=20)
    email=models.EmailField()
    sitio_web =models.URLField()
    fecha_fundacion =models.DateField()
    history= HistoricalRecords()

    def __str__(self):
        return self.nombre
