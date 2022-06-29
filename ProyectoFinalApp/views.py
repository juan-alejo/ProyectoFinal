from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import *
from .forms import *


# Create your views here.

def inicio(request):

    return render(request,'ProyectoFinalApp/index.html')

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
    

def juegos(request):
    
    if request.method == "POST":
        
        search = request.POST["search"]
        
        if search !="":
            juegos = Juego.objects.filter( Q(nombre__icontains=search)| Q(genero__icontains=search) ).values()
            
            return render(request, "ProyectoFinalApp/juegos.html",{"juegos":juegos, "search":True, "busqueda":search})
    
    juegos = Juego.objects.all()
    
    return render(request,"ProyectoFinalApp/juegos.html",{"juegos":juegos})

def crearJuego(request):
 
    #post
    if request.method == "POST":
        
        formularioJuego = NuevoJuego(request.POST)
        
        if formularioJuego.is_valid():
            
            infoJuego = formularioJuego.cleaned_data
        
            juego = Juego(nombre = infoJuego["nombre"], genero = (infoJuego["genero"]))
            
            juego.save()
            
            return redirect("juegos") 
        
        else:
            return render(request,"ProyectoFinalApp/formularioJuego.html",{"form":formularioVacio})
    
    
    else: #get y otros
        
        formularioVacio = NuevoJuego()
        
        
        return render(request,"ProyectoFinalApp/formularioJuego.html",{"form":formularioVacio})
    
    
    
def eliminarJuego(request, juego_id):
    
    juego = Juego.objects.get(id=juego_id)
    juego.delete()
    
    return redirect("juegos")

def editarJuego(request, juego_id):
    
    
    juego = Juego.objects.get(id=juego_id)

    if request.method == "POST":
        
        formulario = NuevoJuego(request.POST)
        
        if formulario.is_valid():
            
            infoJuego = formulario.cleaned_data
            
            juego.nombre = infoJuego["nombre"]
            juego.genero = infoJuego["genero"]
            juego.save()
            
            return redirect("juegos")
        
        
    formulario = NuevoJuego(initial={"nombre":juego.nombre, "genero":juego.genero})
    
    return render(request,"ProyectoFinalApp/formularioJuego.html",{"form":formulario})

class JuegoList(ListView):
    
    model = Juego
    template_name = "ProyectoFinalApp/juegosList.html"
    
class JuegoDetail(DetailView):
    
    model = Juego
    template_name = "ProyectoFinalApp/juegoDetail.html"
    
class JuegoCreate(CreateView):
    
    model = Juego
    success_url = "/app/list"   #Atención a la primer barra
    fields = ["nombre", "genero"]
    
    
class JuegoUpdate(UpdateView):
    model = Juego
    success_url = "/app/list"   #Atención a la primer barra
    fields = ["nombre", "genero"]
    
class JuegoDelete(UpdateView):
    model = Juego
    success_url = "/app/list"   #Atención a la primer barra
    