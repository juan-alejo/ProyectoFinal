from django.urls import path

from .views import *

urlpatterns = [
    # URLS de la app
    path('', inicio, name="inicio"),

    #path('profesores/', profesores, name="profesores"),
]