from django.db import models

# Create your models here.
class Departamento(models.Model): # un modelo de los modelos que ya existen
    # CharFiels pa intraducir texto y length maximo a 50 caracteres y nombre: es lo que aparecera para indicar la entrada
    # blank=True para q el campo de texto no sea obligatorio
    # null=True para q el campo de imagenes no sea obligatio
    # unique = True para que el campo sea unico y no pueda repetir 
    # editable=False para que no se pueda editar este campo
    
    name = models.CharField('Nombre', max_length=50) 
    shor_name = models.CharField('Nombre Corto', max_length=20)
    anulate = models.BooleanField('Anulado', default=False)
        
    # para modificar el panel del admin
    class Meta:
        verbose_name = 'Mi Departamento' # modificar el nombre de la base en el admin 
        verbose_name_plural = 'Despartamentos' # modificar el nombre de la base cuando esta en plural
        # ordering = ['name'] # para ordenar la lista dentro de la base
        unique_together = ('name', 'shor_name') # para indicar los parametro que seran unicos en cada registro

    def __str__(self):
        return str(self.id) + '_' + self.name + '_' + self.shor_name # lo que quieres pedir que se vea en el panel del admin
