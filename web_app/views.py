from django.shortcuts import render


# Create your views here.
from servicios.models import Servicio


def home(request):
    return render(request, 'home.html')





def tienda(request):
    return render(request, 'tienda.html')


def blog(request):
    return render(request, 'blog.html')


def contacto(request):
    return render(request, 'contacto.html')
