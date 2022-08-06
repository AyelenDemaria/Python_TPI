from django.urls import path
from . import views


urlpatterns = [
    path('', views.instalacion_list, name='instalacion_list'),
]
