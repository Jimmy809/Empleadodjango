from django import forms
from django.urls import reverse_lazy

class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    shorname = forms.CharField(max_length=20)
    success_url = reverse_lazy('persona_app:empleados_admin')
    