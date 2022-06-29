from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NuevoServidor(forms.Form):
    nombre = forms.CharField(max_length = 25, label = "Nombre del servidor")
    version = forms.IntegerField(min_value = 0, label = "Versión del servidor")
    
class NuevoJugador(forms.Form):
    nombre = forms.CharField(max_length= 15, label = "Nombre")
    apellido = forms.CharField(max_length= 15, label = "Apellido")
    edad = forms.IntegerField(min_value= 0, label = "Edad")
    usuario = forms.CharField(max_length= 15, label = "Nombre de usuario")
    
class NuevoJuego(forms.Form):
    nombre = forms.CharField(max_length=25, label= "Nombre del juego")
    genero = forms.CharField(max_length=25, label= "Género")
    
    

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget = forms.PasswordInput) # widget.PasswordInput -> Hace que la contraseña no se vea
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        help_texts = {k:"" for k in fields}
        
    
