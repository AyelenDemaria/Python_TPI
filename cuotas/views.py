from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from . import views
from usuarios.models import Perfil
from .models import Cuota
from django.contrib.auth.models import User
from templates import cuotas
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.db.models import Q
from django.utils import timezone
from decimal import Decimal

#from payments import get_payment_model

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

@login_required
def mis_cuotas(request):
    mis_cuotas = Cuota.objects.filter(perfil__user=request.user)

    if not mis_cuotas:
        messages.info(request, "No cuentas con cuotas generadas")

    return render(request, 'cuotas/mis_cuotas.html', {'mis_cuotas':mis_cuotas})

def reporte_pagos(request):
    anio_actual = datetime.today().year
    resultado = []
    for i in range(1,13):
        sum_cobrado = 0
        sum_a_cobrar = 0
        cuotas_a_cobrar = Cuota.objects.filter(anio = anio_actual, mes = i)

        #si tiene algo a cobrar hago todo el resto, de lo contrario no aplica porque significa que no hay cuotas generadas
        if cuotas_a_cobrar:
            for j in cuotas_a_cobrar:
                sum_a_cobrar += j.importe
            cuotas_pagas = cuotas_a_cobrar.filter(fecha_pago__isnull=False)
            #si tiene algo pago calculo, de lo contrario queda en 0 lo pagado (seteado arriba)
            if cuotas_pagas:
                for k in cuotas_pagas:
                    sum_cobrado += k.importe

            resultado.append([meses[i-1],sum_a_cobrar,sum_cobrado,sum_a_cobrar-sum_cobrado])

    return render(request, 'cuotas/reporte_pagos.html', {'resultado': resultado, 'anio_actual': anio_actual})

def reporte_morosos(request):
    socios = Perfil.objects.all()
    resultado = []
    for i in socios:
        sum = 0
        cuotas_pendientes = Cuota.objects.filter(perfil_id = i.id, fecha_pago__isnull=True)
        #si tiene algo pendiente sumo sino no me importa porque es de los morosos
        if cuotas_pendientes:
            for j in cuotas_pendientes:
                sum += j.importe
            print('1', i, cuotas_pendientes.count())
            resultado.append([i,sum,cuotas_pendientes.count()])

    resultado.sort(key = lambda resultado: resultado[2], reverse=True)

    #ver cómo los ordeno por el sum de mayor a menor
    return render(request, 'cuotas/reporte_morosos.html', {'resultado': resultado})
