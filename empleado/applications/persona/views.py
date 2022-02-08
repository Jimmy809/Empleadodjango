from ast import Delete
from dataclasses import field
from pprint import pp
from winreg import DeleteValue
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
# Create your views here.
from .models import Empleado
from django.urls import reverse_lazy
from .forms import EmpleadoForm

class InicioView(TemplateView):
    """ Vista que carga la pagina de inicio """
    template_name = 'inicio.html'

class ListAllEplemados(ListView): # para listar todos los empleados
    template_name = 'persona/list_all.html'
    paginate_by = 4 # para que muestre una cantidad deteminada y paginarlas
    ordering = 'first_name'
    
    context_object_name = 'empleados'

    def get_queryset(self):
        # print('*********')
        palabra_clave = self.request.GET.get("kword", '')
        # print('=======', palabra_clave)
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        # print('lista resultado:', lista)
        return lista
    
    
class ListEmpleadosAdmin(ListView):  # para listar todos los empleados
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10  # para que muestre una cantidad deteminada y paginarlas
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado

    

class ListByArea(ListView): # lista de empleados por un area
    template_name = 'persona/listar-by-area.html'
    context_object_name = 'empleados'
    # para listar por departamento
    # queryset = Empleado.objects.filter(
    #     # contabilidad es el departamento, pero si queremos otro solo has q cambiarlo
    #     departamento__shor_name = 'contabilidad'
    # )

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista
    
class ListEmpleadosByKword(ListView):
    ''' lista empleado por palabra clave'''
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('*********')
        palabra_clave = self.request.GET.get("kword", '')
        print('=======', palabra_clave)
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        # print('lista resultado:', lista)
        return lista
    
class ListHablilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)        
        return empleado.habilidades.all()
    

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context["titulo"] = 'Empleado del mes'
        return context
    

class SuccessView(TemplateView):
    template_name = "persona/success.html"
    

class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    form_class = EmpleadoForm
    # fields = [
    #     'first_name', 
    #     'last_name', 
    #     'job', 
    #     'departamento', 
    #     'habilidades',
    #     'avatar',
    # ] # especificar lo que quieres
    # fields = ('__all__') # para pedir todo
    # success_url = '/success'
    success_url = reverse_lazy('persona_app:empleados_admin')
    
    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    

class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades'
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request,  *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):    
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')
