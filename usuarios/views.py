from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from usuarios.models import Usuario
from . import views

# Create your views here.
def index(request):
    return render(request, 'instalacion_list.html')

def login_template(request,error=False):
    return render(request,'login.html',context={'error':error})


def login_view(request):
    email = request.POST['email']
    contreaseña = request.POST['contraseña']
    user = authenticate(request, email=email, contraseña=contraseña)
    if user is not None:
        login(request,user)
        return redirect(reverse(views.index))
    else:
        return login_template(request,True)
