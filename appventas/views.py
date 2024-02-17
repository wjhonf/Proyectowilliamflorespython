from django.shortcuts import render
from appventas.models import Equipo, Cliente
from django.http import HttpResponse
from appventas.forms import EquipoFormulario, Buscar, ClienteFormulario
# Create your views here.

def inicio(request):
     return  render(request, "appventas/index.html")
def equipos(request):
    return  render(request, "appventas/equipos.html")

def equipo_form(request):
    if request.method=='POST':
        equipo= Equipo(nombre=request.POST['nombre'],descripcion=request.POST['descripcion'],imagen=request.POST['imagen'],precio=request.POST['precio'])
        equipo.save()
        return render(request, "appventas/index.html")
    return  render(request, "appventas/equipo_formulario.html")

def equipo_form2(request):
    if request.method == "POST":
        miFormulario = EquipoFormulario(request.POST) 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            equipo_objeto = Equipo(
                nombre=informacion['nombre'],
                descripcion=informacion['descripcion'],
                imagen=informacion['imagen'],
                precio=informacion['precio']
            )
            equipo_objeto.save()
            return render(request, "appventas/index.html")
    else:
        miFormulario = EquipoFormulario()

    return render(request, "appventas/equipoFormulario.html", {"formulario": miFormulario})

def buscar(request):
    if request.method == 'POST':
         miFormulario= Buscar(request.POST)
         if miFormulario.is_valid():
             info= miFormulario.cleaned_data
             objequipos =Equipo.objects.filter(nombre__icontains=info["nombre"])
             return render(request, "appventas/buscar.html", {"formulario": miFormulario, "equipo": objequipos})
             
    else:
        miFormulario = Buscar()
    return render(request, "appventas/buscar.html", {"formulario": miFormulario})

def cliente_form(request):
    if request.method == "POST":
        miFormulario = ClienteFormulario(request.POST) 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cliente_objeto = Cliente(
                nombre=informacion['nombre'],
                direccion =informacion['direccion'],
                correo_electronico =informacion['correo_electronico'],
            )
            cliente_objeto.save()
            return render(request, "appventas/index.html")
    else:
        miFormulario = ClienteFormulario()

    return render(request, "appventas/clienteFormulario.html", {"formulario": miFormulario})
    
    
    
    
