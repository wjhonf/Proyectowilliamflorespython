from django.contrib import admin
from appventas.models import Equipo,Cliente, Venta, DetalleVenta
# Register your models here.
admin.site.register(Equipo)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
