from django.urls import path
from . import views


urlpatterns = [

    path('pago/', views.payment_details, name='payment_details'),


]
