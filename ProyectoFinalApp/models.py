from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Servidor(models.Model):
    nombre = models.CharField(max_length = 20) #texto
    version = models.IntegerField() #numerico
    
    class Meta:
        verbose_name_plural = "Servidores"
        

class Jugador(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    edad = models.IntegerField()
    usuario = models.CharField(max_length = 25)
    
    class Meta:
        verbose_name_plural = "Jugadores"
        
        
class Juego(models.Model):
    nombre = models.CharField(max_length = 20)
    genero = models.CharField(max_length = 20)
    
    class Meta:
        verbose_name_plural = "Juegos"
        
        
class Avatar(models.Model):
    
    usuario = models.OneToOneField(User, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatars', blank = True, null = True)