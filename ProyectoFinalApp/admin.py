from django.contrib import admin

from .models import *

# Register your models here.


class ServidorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'version', 'juegoServer')
    search_fields = ('nombre', 'version', 'juegoServer')
    
    
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'usuario', 'edad')
    saerch_fields = ('nombre', 'apellido', 'usuario', 'edad')
    
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'genero')
    saerch_fields = ('nombre', 'genero')
    
class AvatarAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'imagen')
    search_fields = ('usuario', 'imagen')
    
    
admin.site.register(Servidor, ServidorAdmin)
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Juego, JuegoAdmin)
admin.site.register(Avatar, AvatarAdmin)