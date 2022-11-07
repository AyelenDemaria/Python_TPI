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

from payments import get_payment_model


@login_required
def mis_cuotas(request):
    mis_cuotas = Cuota.objects.filter(perfil__user=request.user)

    if not mis_cuotas:
        messages.info(request, "No cuentas con cuotas generadas")

    return render(request, 'cuotas/mis_cuotas.html', {'mis_cuotas':mis_cuotas})

def pagar_cuota(request,pk):
    Payment = get_payment_model()
    payment = Payment.objects.create(
        variant='default',  # this is the variant from PAYMENT_VARIANTS
        description='cuota',
        total=Decimal(120),
        tax=Decimal(20),
        currency='ARS',
        delivery=Decimal(10),
        billing_first_name= request.user.first_name,
        billing_last_name= request.user.last_name,
        billing_address_1='',
        billing_address_2='',
        billing_city='San Jose de la Esquina',
        billing_postcode='2185',
        billing_country_code='AR',
        billing_country_area='Argentina',
        customer_ip_address='127.0.0.1',
    )
    cuota = get_object_or_404(Cuota, pk=pk)
    cuota.fecha_pago = timezone.now()
    cuota.save()
    return redirect(reverse(views.mis_cuotas))
