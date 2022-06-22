from django.urls import path

from .views import *

urlpatterns = [
    # URLS de la app
    path('', inicio, name="inicio"),
    path('servidores/', servidores, name= "servidores"),
    path('crearservidor/', crearServidor, name= "crearServidor"),
    path('jugadores/', jugadores, name= "jugadores"),
    path('crearjugador/', crearJugador, name= "crearJugador"),
]