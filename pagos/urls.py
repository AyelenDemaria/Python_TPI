from django.urls import path
from . import views


urlpatterns = [

    path('pago/<int:pk>/', views.payment_details, name='payment_details'),


]
