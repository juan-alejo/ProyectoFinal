from django import forms

class NuevoServidor(forms.Form):
    nombre = forms.CharField(max_length = 25, label = "Nombre del servidor")
    version = forms.IntegerField(min_value = 0, label = "Versión del servidor")