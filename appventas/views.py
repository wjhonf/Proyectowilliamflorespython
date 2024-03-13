from django.shortcuts import render,redirect, get_object_or_404
from appventas.models import  Cliente, Equipo, Venta,DetalleVenta
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

from django.views import View
import json
from appventas.forms import EquipoFormulario, Buscar, ClienteFormulario, EditarEquipo
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

def inicio(request):
     return  render(request, "appventas/index.html")
 
class NosotrosView(View):
    def get(self, request):
        return render(request, "appventas/nosotros.html")


class EquipoFormView(View):
    @method_decorator(login_required)
    def get(self, request):
        miFormulario = EquipoFormulario()
        return render(request, "appventas/equipoFormulario.html", {"formulario": miFormulario})
    @method_decorator(login_required)
    def post(self, request):
        miFormulario = EquipoFormulario(request.POST, request.FILES) 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            equipo_objeto = Equipo(
                nombre=informacion['nombre'],
                descripcion=informacion['descripcion'],
                imagen=request.FILES['imagen'],
                precio=informacion['precio']
            )
            equipo_objeto.save()
            messages.success(request, 'Equipo registrado correctamente.')
            return redirect("list_equipos") 
        return render(request, "appventas/equipoFormulario.html", {"formulario": miFormulario})

class ListEquiposView(View):
    @method_decorator(login_required)
    def get(self, request):
        equipos = Equipo.objects.all()
        miFormulario = Buscar()
        return render(request, "appventas/list_equipos.html", {"formulario": miFormulario, "equipos": equipos})
    @method_decorator(login_required)
    def post(self, request):
        equipos = Equipo.objects.all()
        miFormulario = Buscar(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            equipos = equipos.filter(nombre__icontains=info["nombre"]) 
        return render(request, "appventas/list_equipos.html", {"formulario": miFormulario, "equipos": equipos})

class CatalogEquiposView(View):
    @method_decorator(login_required)
    def get(self, request):
        equipos = Equipo.objects.all()
        miFormulario = Buscar()
        equipos_json = serialize('json', equipos)
        return render(request, "appventas/catalog_equipos.html", {"formulario": miFormulario, "equipos_json": equipos_json})
    @method_decorator(login_required)
    def post(self, request):
        equipos = Equipo.objects.all()
        miFormulario = Buscar(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            equipos = equipos.filter(nombre__icontains=info["nombre"]) 
        equipos_json = serialize('json', equipos)
        return render(request, "appventas/catalog_equipos.html", {"formulario": miFormulario, "equipos_json": equipos_json})

class EliminarEquipoView(View):
    @method_decorator(login_required)
    def post(self, request, equipo_id):
        equipo = get_object_or_404(Equipo, pk=equipo_id)
        equipo.delete()
        messages.success(request, 'El equipo ha sido eliminado exitosamente.')
        return redirect('list_equipos')

class EditarEquipoView(View):
    @method_decorator(login_required)
    def post(self, request, equipo_id):
        equipo = get_object_or_404(Equipo, pk=equipo_id)
        formulario = EditarEquipo(request.POST, request.FILES, instance=equipo)
        if formulario.is_valid():
            formulario.save()
        else:
            print(formulario.errors)
        return redirect('list_equipos')

class ClienteFormView(View):
    @method_decorator(login_required)
    def get(self, request):
        miFormulario = ClienteFormulario()
        return render(request, "appventas/clienteFormulario.html", {"formulario": miFormulario})
    @method_decorator(login_required)
    def post(self, request):
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
        return render(request, "appventas/clienteFormulario.html", {"formulario": miFormulario})

class ObtenerClientesView(View):
    @method_decorator(login_required)
    def get(self, request):
        clientes = Cliente.objects.all().values('id', 'nombre', 'direccion', 'correo_electronico')
        return JsonResponse(list(clientes), safe=False)


class GuardarVentaView(View):
    @method_decorator(login_required)
    def post(self, request):
        data = json.loads(request.body)
        cliente_id  = data.get('nombre_cliente')
        email = data.get('email_cliente')
        numero_tarjeta = data.get('numero_tarjeta')
        fecha_expiracion = data.get('fecha_expiracion')
        cliente = Cliente.objects.get(pk=cliente_id)
        venta = Venta(cliente=cliente, email=email, numero_tarjeta=numero_tarjeta, fecha_expiracion=fecha_expiracion)
        venta.save()
        equipos = data.get('equipos', [])
        for equipo_data in equipos:
            equipo_id = equipo_data.get('id')
            cantidad = equipo_data.get('cantidad')
            equipo = Equipo.objects.get(pk=equipo_id)
            detalle_venta = DetalleVenta(venta=venta, equipo=equipo, cantidad=cantidad)
            detalle_venta.save()
        return JsonResponse({'mensaje': 'Venta guardada correctamente.', 'redirect_url': '/appventas/catalog_equipos/'})







    
    
