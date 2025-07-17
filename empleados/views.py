
from django.shortcuts import render
from .models import Empleado, Portfolio


def index(request):
    return render(request, 'empleados/index.html')
def empleados_list(request):
    empleados = Empleado.objects.select_related('departamento')
    return render(request, 'empleados/list.html', {'empleados': empleados})

def empleados_create(request):
    return render(request, 'empleados/new.html')

def portfolio_list(request): #FBV
    portfolios = Portfolio.objects.all()
    return render(request, 'empleados/portfolio.html', {'portfolios': portfolios})