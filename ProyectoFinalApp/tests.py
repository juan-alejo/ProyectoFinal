from django.test import TestCase
from .models import *

# Create your tests here.

class JugadoresTestCase(TestCase):
    def setUp(self):
        self.jugador = Jugador.objects.create(nombre = 'Juan', apellido = 'Perez', edad = 20, usuario = 'juanperez')
        
    def test_jugador_nombre(self):
        self.assertEqual(self.jugador.nombre, 'Juan')