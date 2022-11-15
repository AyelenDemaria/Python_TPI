from django.conf import settings
from django.utils import timezone
from django.db import models
from django.apps import AppConfig
from usuarios.models import Perfil

# Create your models here.    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)

class Cuota(models.Model):
    mes = models.IntegerField(default=0, null=False)
    anio =  models.IntegerField(default=0, null=False)
    fecha_pago = models.DateTimeField(null=True, blank=True)
    importe = models.DecimalField(max_digits=5, decimal_places=2)
    #usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    perfil= models.ForeignKey(Perfil, on_delete=models.SET_NULL, null=True)

    def __str__(self):

        return str(self.mes) + '  -  ' + str(self.anio) + ' - ' + str(self.perfil.user.username) + ' - ' + str(self.perfil.documento)
