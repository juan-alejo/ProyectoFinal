from django.contrib import admin

from .models import *

# Register your models here.


class ServidorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'version')
    search_fields = ('nombre', 'version')
    
    
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'usuario', 'edad')
    saerch_fields = ('nombre', 'apellido', 'usuario', 'edad')
    
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'genero')
    saerch_fields = ('nombre', 'genero')
    
    
admin.site.register(Servidor, ServidorAdmin)
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Juego, JuegoAdmin)

admin.site.register(Avatar)