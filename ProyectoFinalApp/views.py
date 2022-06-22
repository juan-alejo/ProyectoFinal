from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import *
from .forms import *


# Create your views here.

def inicio(request):

    return render(request,'ProyectoFinalApp\index.html')

def servidores(request):
    
    #servidores = Servidor()
    
    #listaServidores = [x.nombre for x in Servidor.objects.all()]
    
    #return HttpResponse((f"Servidores: {str(listaServidores)}"))
    
    servidores = Servidor.objects.all()
    
    return render(request,"ProyectoFinalApp/servidores.html",{"servidores":servidores})