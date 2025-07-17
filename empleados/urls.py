from django.urls import path
from . import views

urlpatterns = [

path('', views.index, name='index'),
path('empleados/', views.empleados_list, name='empleados'),
path('nuevo/', views.empleados_create, name='nuevo'),
path('portfolio/', views.portfolio_list, name='portfolio'),
]