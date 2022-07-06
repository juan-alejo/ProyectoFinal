from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import *
from .forms import *


# Create your views here.

@login_required
def agregarAvatar(request):
    
    if request.method == "POST":
            
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            user = User.objects.get(username=request.user.username) # usuario con el que estamos loggueados

            avatar = Avatar(usuario=user, imagen=form.cleaned_data["imagen"])

            avatar.save()

            return redirect("inicio")

    else:
        form = AvatarForm()
    
    return render(request,"ProyectoFinalApp/agregarAvatar.html",{"form":form})
    
    
    

def inicio(request):

    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(usuario=request.user)
            url = avatar.imagen.url
        except:
            url = "/media/avatars/default.png"
            
        return render(request,"ProyectoFinalApp/index.html",{"url":url})
    
    return render(request,'ProyectoFinalApp/index.html')

def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
            
        else:
            return redirect("login")
            
    form = AuthenticationForm()
    
    return render(request,"ProyectoFinalApp/login.html", {"form":form})

def register_request(request):
    
    if request.method == "POST":
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            form.save()
            
            messages.success(request, "Usuario registrado correctamente")
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
            
        
        return render(request,"ProyectoFinalApp/register.html", {"form":form})
    
    form = UserRegisterForm()
    
    return render(request,"ProyectoFinalApp/register.html", {"form":form})

@login_required
def logout_request(request):
    logout(request)
    return redirect('inicio')
 
@login_required    
def editarPerfil(request):
    
    user = request.user  #Usuario con el que estoy logeado
    
    if request.method == "POST":
        
        form = UserEditForm(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            
            user.save()
            
            messages.success(request, "Perfil editado correctamente")
            
            return redirect("inicio")
        
        return render(request,"ProyectoFinalApp/editarPerfil.html",{"form":form})   
     
    else:
        form = UserEditForm(initial = {"email":user.email, "first_name":user.first_name, "last_name":user.last_name})
    
    return render(request,"ProyectoFinalApp/editarPerfil.html",{"form":form})

def servidores(request):
    
    if request.method == "POST":
        
        search = request.POST["search"]
        
        if search !="":
            servidores = Servidor.objects.filter( Q(nombre__icontains=search)| Q(version__icontains=search)| Q(juegoServer__icontains=search) ).values()
            
            return render(request, "ProyectoFinalApp/servidores.html",{"servidores":servidores, "search":True, "busqueda":search})
    
    servidores = Servidor.objects.all()
    
    return render(request,"ProyectoFinalApp/servidores.html",{"servidores":servidores})

def crearServidor(request):
 
    #post
    if request.method == "POST":
        
        formularioServidor = NuevoServidor(request.POST)
        
        if formularioServidor.is_valid():
            
            infoServidor = formularioServidor.cleaned_data
        
            servidor = Servidor(nombre = infoServidor["nombre"], version =int(infoServidor["version"]), juegoServer = infoServidor["juegoServer"])
            
            servidor.save()
            
            messages.success(request, "Servidor creado correctamente")
            
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
            
            messages.success(request, "Jugador creado correctamente")
            
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
            
            messages.success(request, "Juego creado correctamente")
            
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

def editarServidor(request, servidor_id):
    
    
    servidor = Servidor.objects.get(id=servidor_id)

    if request.method == "POST":
        
        formulario = NuevoServidor(request.POST)
        
        if formulario.is_valid():
            
            infoServidor = formulario.cleaned_data
            
            servidor.nombre = infoServidor["nombre"]
            servidor.version = infoServidor["version"]
            servidor.juegoServer = infoServidor["juegoServer"]
            servidor.save()
            
            return redirect("servidores")
        
        
    formulario = NuevoServidor(initial={"nombre":servidor.nombre, "version":servidor.version, "juegoServer":servidor.juegoServer})
    
    return render(request,"ProyectoFinalApp/formularioServidor.html",{"form":formulario})

def about(request):
    return render(request,"ProyectoFinalApp/about.html")

class JuegoList(LoginRequiredMixin,ListView):
    
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
    
class JuegoDelete(DeleteView):
    model = Juego
    success_url = "/app/juegos"   #Atención a la primer barra
    
    
class ServidorList(ListView):
    
    model = Servidor
    template_name = "ProyectoFinalApp/servidoresList.html"

class ServidorDetail(DetailView):
    
    model = Servidor
    template_name = "ProyectoFinalApp/servidorDetail.html"
    
class ServidorCreate(CreateView):
    
    model = Servidor
    success_url = "/app/servidores"   
    fields = ["nombre", "version"]
    
    
class ServidorUpdate(UpdateView):
    model = Servidor
    success_url = "/app/servidores"   
    fields = ["nombre", "version"]
    
class ServidorDelete(DeleteView):
    model = Servidor
    success_url = "/app/servidores"   