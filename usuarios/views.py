from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
#from usuarios.models import Usuario
from . import views
from instalaciones.models import Instalacion
from templates import instalaciones,registration

# Create your views here.
def index(request):
    instalaciones = Instalacion.objects.all()
    return render(request, 'instalaciones/instalacion_list.html',{'instalaciones':instalaciones})


def login_template(request,error=False):
    return render(request,'registration/login.html',context={'error':error})



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.error(request, "Invalido username o clave")
        else:
            messages.error(request, "Invalido username o password")
    form = AuthenticationForm()
    return render (request=request, template_name="registration/login.html",context={"login_form":form})

@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse(views.login_view))
