from django.contrib import admin

from empleados.models import Empleado, Departamento


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'departamento')
    list_filter = ('departamento',)

admin.site.register(Departamento)
