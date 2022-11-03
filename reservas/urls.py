from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('reservar/<int:pk>/', views.nueva_reserva, name='nueva_reserva'),
    path('reservas/', views.mis_reservas, name='mis_reservas'),
    path('cancelar/<int:pk>/', views.cancelar_reserva, name='cancelar_reserva'),
]
