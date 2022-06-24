from django.urls import path

from .views import *

urlpatterns = [
    # URLS de la app
    path('', inicio, name="inicio"),
    path('servidores/', servidores, name= "servidores"),
    path('crearservidor/', crearServidor, name= "crearServidor"),
    path('jugadores/', jugadores, name= "jugadores"),
    path('crearjugador/', crearJugador, name= "crearJugador"),
    path('crearjuego/', crearJuego, name= "crearjuego"),
    path('eliminarjuego/<juego_id>', eliminarJuego, name = "eliminarJuego"),
    path('editarJuego/<juego_id>', editarJuego, name = "editarJuego"),
    
    path('juegos/', juegos, name= "juegos"),
    path(r'list', JuegoList.as_view(), name = "juegoList"),
    path(r'^(?P<pk>\d+)$', JuegoDetail.as_view(), name = "juegoDetail"),       ###
    path(r'^nuevo$', JuegoCreate.as_view(), name = "juegoCreate"), ###3
    path(r'^editar/(?P<pk>\d+)$', JuegoUpdate.as_view(), name = "juegoUpdate"),       ###
    path(r'^eliminar/(?P<pk>\d+)$', JuegoDelete.as_view(), name = "juegoDelete"),       ###
]