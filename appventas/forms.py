from django import forms
class EquipoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=100)  
    imagen = forms.CharField(max_length=100)  
    precio = forms.DecimalField(max_digits=10, decimal_places=2)

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=20)
    
class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=200)
    correo_electronico = forms.EmailField()