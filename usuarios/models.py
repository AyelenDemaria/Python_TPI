from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

"""class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=False)
    documento = models.CharField(max_length=8)
    direccion = models.CharField(max_length=100,blank=True, null=True)
    telefono = models.CharField(max_length=20,blank=True, null=True)
    email = models.EmailField(null=False)
    contraseña = models.CharField(max_length=50)
"""

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    documento = models.CharField(max_length=8)


    def __str__(self):
        return self.documento 
