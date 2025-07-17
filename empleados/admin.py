from django.contrib import admin

from empleados.models import Empleado, Departamento, Portfolio


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'departamento')
    list_filter = ('departamento',)

admin.site.register(Departamento)
admin.site.register(Portfolio)
