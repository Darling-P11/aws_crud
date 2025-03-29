from django.db import models

class Imagen(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_detectado = models.CharField(max_length=100, blank=True)
    descripcion = models.TextField(blank=True)
    archivo = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return self.nombre
