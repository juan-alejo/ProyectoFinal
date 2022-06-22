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
        
   # return HttpResponse("asd")