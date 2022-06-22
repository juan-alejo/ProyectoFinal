from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import *
from .forms import *


# Create your views here.

def inicio(request):

    return render(request,'ProyectoFinalApp\index.html')

def servidores(request):
    
    servidores = Servidor.objects.all()
    
    return render(request,"ProyectoFinalApp/servidores.html",{"servidores":servidores})


def crearServidor(request):
 
    #post
    if request.method == "POST":
        
        formularioServidor = NuevoServidor(request.POST)
        
        if formularioServidor.is_valid():
            
            infoServidor = formularioServidor.cleaned_data
        
            servidor = Servidor(nombre = infoServidor["nombre"], version =int(infoServidor["version"]))
            
            servidor.save()
            
            return redirect("servidores") 
        
        else:
            return render(request,"ProyectoFinalApp/formularioServidor.html",{"form":formularioVacio})
    
    
    else: #get y otros
        
        formularioVacio = NuevoServidor()
        
        
        return render(request,"ProyectoFinalApp/formularioServidor.html",{"form":formularioVacio})

def jugadores(request):
    
    jugadores = Jugador.objects.all()
    
    return render(request,"ProyectoFinalApp/jugadores.html",{"jugadores":jugadores})


def crearJugador(request):
 
    #post
    if request.method == "POST":
        
        formularioJugador = NuevoJugador(request.POST)
        
        if formularioJugador.is_valid():
            
            infoJugador = formularioJugador.cleaned_data
        
            jugador = Jugador(nombre = infoJugador["nombre"], apellido=(infoJugador["apellido"]), usuario=(infoJugador["usuario"]), edad=(infoJugador["edad"]))
            
            jugador.save()
            
            return redirect("jugadores") 
        
        else:
            return render(request,"ProyectoFinalApp/formularioJugadores.html",{"form":formularioVacio})
    
    
    else: #get y otros
        
        formularioVacio = NuevoJugador()
        
        
        return render(request,"ProyectoFinalApp/formularioJugadores.html",{"form":formularioVacio})