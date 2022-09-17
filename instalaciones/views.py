from django.shortcuts import render
from .models import Instalacion
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def instalacion_list(request):
    instalaciones = Instalacion.objects.order_by('importe')
    return render(request, 'instalaciones/instalacion_list.html', {'instalaciones':instalaciones})
