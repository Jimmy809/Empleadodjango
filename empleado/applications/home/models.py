from django.db import models

# Create your models here.

class Prueba(models.Model): #nombre de la tabla
    titulo = models.CharField(max_length=100) # categorias o parametro que va a a tener
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return self.titulo + ' ' + self.subtitulo