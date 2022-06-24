from django.urls import path

from .views import *

urlpatterns = [
    # URLS de la app
    path('', inicio, name="inicio"),
    path('servidores/', servidores, name= "servidores"),
    path('crearservidor/', crearServidor, name= "crearServidor"),
    path('jugadores/', jugadores, name= "jugadores"),
    path('crearjugador/', crearJugador, name= "crearJugador"),
    path('juegos/', juegos, name= "juegos"),
    path('crearjuego/', crearJuego, name= "crearjuego"),
    path('eliminarjuego/<juego_id>', eliminarJuego, name = "eliminarJuego"),
    path('editarJuego/<juego_id>', editarJuego, name = "editarJuego"),
]