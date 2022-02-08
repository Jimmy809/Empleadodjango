from django.db import models
from applications.departamento.models import Departamento # 1 importamos la base de datos que queremos vincular
from django.db import models
from ckeditor.fields import RichTextField


class Habilidades(models.Model):
    hablidades = models.CharField('habilidades', max_length=50,)
    
    class meta:
        verbose_name = 'Habilidad'  # modificar el nombre de la base en el admin
        # modificar el nombre de la base cuando esta en plural
        verbose_name_plural = 'Habilidades Empleados'
        
    def __str__(self):
        return str(self.id) + ' - ' + self.hablidades

# Create your models here.
class Empleado(models.Model):
    job_choices = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
       
    )
    ''' Modelo para tabla empleado '''
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField(
        'Nombres completos', 
        max_length=120,
        blank=True,
    )

    # choices para agrergar una lista predefinida ya declarada arriba job_choices
    job = models.CharField('Trabajo', max_length=50, choices=job_choices)
    # 1.1 con models.ForeignKey creamos la vinculacion con la tampla departamento
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    # 1.2 con models.ManyToManyField relacionamos muchas bases con muchas bases (que se relacionen entre si)
    habilidades = models.ManyToManyField(Habilidades)  
    hoja_vida = RichTextField()
    
    class Meta:
        verbose_name = 'Mi Empleado'  # modificar el nombre de la base en el admin
        # modificar el nombre de la base cuando esta en plural
        verbose_name_plural = 'Mis Empleados'
        # ordering = ['name']  # para ordenar la lista dentro de la base
        # para indicar los parametro que seran unicos en cada registro
        # unique_together = ('name', 'shor_name')

    def __str__(self):
        return str(self.id) + '_' + self.first_name + '_' + self.last_name
