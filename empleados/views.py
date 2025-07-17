
from django.shortcuts import render
from .models import Empleado

def empleados_list(request):
    empleados = Empleado.objects.select_related('departamento')
    return render(request, 'empleados/index.html', {'empleados': empleados})