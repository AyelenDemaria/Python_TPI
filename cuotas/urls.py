from django.urls import path
from . import views


urlpatterns = [

    path('cuotas/', views.mis_cuotas, name='mis_cuotas'),
    path('pagar_cuota/', views.pagar_cuota, name='pagar_cuota'),

]
