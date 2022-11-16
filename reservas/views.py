from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from . import views
from instalaciones.models import Instalacion
from usuarios.models import Perfil
from cuotas.models import Cuota
from .models import Reserva
from django.contrib.auth.models import User
from templates import instalaciones, reservas
from django.shortcuts import get_object_or_404
from .forms import NuevaReserva
from datetime import datetime
from django.db.models import Q
from django.utils import timezone

def index(request):
    instalaciones = Instalacion.objects.all()
    return render(request, 'instalaciones/instalacion_list.html',{'instalaciones':instalaciones})

@login_required
def nueva_reserva(request,pk):
    inst = get_object_or_404(Instalacion, pk=pk)
    if request.method == "POST":

        form = NuevaReserva(request.POST)
        if form.is_valid():

            fhd = form.cleaned_data.get('fecha_hora_desde')
            fhh = form.cleaned_data.get('fecha_hora_hasta')
            year = datetime.today().year
            month = datetime.today().month
            id_user = User.objects.get(username = request.user)
            perfil = Perfil.objects.get(user_id=id_user)
            cuotas_debe = Cuota.objects.filter(
                                              Q(mes__lt = month),
                                              anio = year,
                                              fecha_pago__isnull = True,
                                              perfil_id = perfil.id)
            if not cuotas_debe:
                inst_reservadas = Reserva.objects.filter(
                                                        Q(fecha_hora_desde__lte = fhd, fecha_hora_hasta__gte = fhh)
                                                        |
                                                        Q(fecha_hora_desde__range=(fhd, fhh))
                                                        |
                                                        Q(fecha_hora_hasta__gt = fhd, fecha_hora_hasta__lte = fhh),
                                                        instalacion_id=pk,fecha_cancelacion__isnull=True)
                if not inst_reservadas:

                    mis_res = Reserva.objects.filter(
                                                    Q(fecha_hora_desde__lte = fhd, fecha_hora_hasta__gte = fhh)
                                                    |
                                                    Q(fecha_hora_desde__range=(fhd, fhh))
                                                    |
                                                    Q(fecha_hora_hasta__gt = fhd, fecha_hora_hasta__lte = fhh),
                                                    perfil_id=perfil.id,fecha_cancelacion__isnull=True)
                    if not mis_res:
                        reserva = form.save(commit=False)
                        reserva.fecha_reserva = timezone.now()
                        reserva.instalacion= inst
                        reserva.perfil = perfil
                        reserva.save()
                        messages.success(request, "Reserva guardada con éxito")
                        return redirect(reverse(views.mis_reservas))
                    else:
                        messages.error(request, "Ya cuentas con una reserva para el periodo seleccionado")
                else:
                    messages.error(request, "Ya existe una reserva para dicha instalacion en el periodo seleccionado")
            else:
                messages.error(request, "Debes tener la cuota al día para reservar")
    form = NuevaReserva()
    return render (request=request, template_name="reservas/nueva_reserva.html",context={"nueva_reserva":form})

@login_required
def mis_reservas(request):
    mis_reservas = Reserva.objects.filter(perfil__user=request.user)

    if not mis_reservas:
        messages.info(request, "No cuentas con reservas realizadas")

    return render(request, 'reservas/mis_reservas.html', {'mis_reservas':mis_reservas})

@login_required
def cancelar_reserva(request,pk):
    res = get_object_or_404(Reserva, pk=pk)
    res.fecha_cancelacion = timezone.now()
    res.save()
    messages.success(request, "Reserva cancelada con éxito")
    return redirect(reverse(views.mis_reservas))
