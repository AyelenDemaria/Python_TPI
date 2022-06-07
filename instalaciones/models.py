from django.conf import settings
from django.db import models
from django.utils import timezone


class Instalacion(models.Model):
    nom_instalacion = models.CharField(max_length=100)
    desc_instalacion =  models.TextField(blank=True, null=True)
    importe = models.DecimalField(max_digits=5, decimal_places=2)
    foto = models.ImageField(upload_to='images', blank=True, null=True)


    def __str__(self):
        return self.nom_instalacion
