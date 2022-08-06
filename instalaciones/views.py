from django.shortcuts import render
from .models import Instalacion

# Create your views here.
def instalacion_list(request):
    instalaciones = Instalacion.objects.order_by('importe')
    return render(request, 'instalaciones/instalacion_list.html', {'instalaciones':instalaciones})
