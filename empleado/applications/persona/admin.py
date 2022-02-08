from re import search
from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.

admin.site.register(Habilidades)

# para mejorar la vista en el panel del admin
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name', 
        'last_name',
        'departamento',
        'job',
        'full_name',
    )    
    
    def full_name(self, obj):
        print(obj.first_name)
        return obj.first_name + ' ' + obj.last_name
    
    search_fields = ('first_name',) # para agregar un buscador
    # para agregar un filtro
    list_filter = ('departamento', 'job', 'habilidades',)
    # para agregar un intercambiador a habilidades
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)
