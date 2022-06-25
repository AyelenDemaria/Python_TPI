from django.conf import settings
from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=False)
    documento = models.CharField(max_length=8)
    direccion = models.CharField(max_length=100,blank=True, null=True)
    telefono = models.CharField(max_length=20,blank=True, null=True)
    email = models.EmailField(null=False)
    contraseña = models.CharField(max_length=50)



    def __str__(self):
        return self.nombre + self.apellido
