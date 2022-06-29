from django.urls import path

from .views import *

urlpatterns = [
    # URLS de la app
    path('', inicio, name="inicio"),
    path('login/', login_request, name="login"),
    path('register/', register_request, name="register"),
    path('logout/', logout_request, name="logout"),
    path('servidores/', servidores, name= "servidores"),
    path('crearservidor/', crearServidor, name= "crearServidor"),
    path('jugadores/', jugadores, name= "jugadores"),
    path('crearjugador/', crearJugador, name= "crearJugador"),
    path('crearjuego/', crearJuego, name= "crearjuego"),
    path('eliminarjuego/<juego_id>', eliminarJuego, name = "eliminarJuego"),
    path('editarJuego/<juego_id>', editarJuego, name = "editarJuego"),
    
    path('juegos/', juegos, name= "juegos"),
    path('juegos/list', JuegoList.as_view(), name = "juegosList"),
    path('juegos/detail/<pk>', JuegoDetail.as_view(), name = "juegoDetail"),       ###
    path('juegos/nuevo', JuegoCreate.as_view(), name = "juegoCreate"), ###3
    path('juegos/editar/<pk>', JuegoUpdate.as_view(), name = "juegoUpdate"),       ###
    path('juegos/eliminar/<pk>', JuegoDelete.as_view(), name = "juegoDelete"),       ###
]