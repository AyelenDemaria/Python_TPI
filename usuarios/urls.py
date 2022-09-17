from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #path('login_template', views.login_template, name='login'),
    path('login', views.login_view, name='login'),
]
