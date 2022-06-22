from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import *
from .forms import *


# Create your views here.

def inicio(request):

    return render(request,'ProyectoFinalApp\index.html')

def crearServidor(request):
    

    return HttpResponse(f"asd")