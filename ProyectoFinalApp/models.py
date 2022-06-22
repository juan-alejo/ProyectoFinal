from django.db import models

# Create your models here.

class Servidor(models.Model):
    nombre = models.CharField(max_length = 20) #texto
    version = models.IntegerField() #numerico
    
    class Meta:
        verbose_name_plural = "Servidores"
        

class Jugador(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    usuario = models.CharField(max_length = 25)
    edad = models.IntegerField()
    