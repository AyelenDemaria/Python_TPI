from django.conf import settings
from django.db import models
from django.utils import timezone
from instalaciones.models import Instalacion
from usuarios.models import Perfil

# Create your models here.
class Reserva(models.Model):
    fecha_reserva = models.DateTimeField(default=timezone.now)
    fecha_hora_desde = models.DateTimeField(null=False)
    fecha_hora_hasta  = models.DateTimeField(null=False)
    fecha_cancelacion  = models.DateTimeField(blank=True, null=True)
    instalacion = models.ForeignKey(Instalacion, on_delete=models.CASCADE)
    #usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    perfil= models.ForeignKey(Perfil, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.fecha_hora_desde) + '-' + str(self.fecha_hora_hasta)
