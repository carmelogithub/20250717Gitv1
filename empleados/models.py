from django.db import models
class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Portfolio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre