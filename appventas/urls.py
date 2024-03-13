from django.urls import path
from appventas.views import  NosotrosView,EquipoFormView,ListEquiposView,CatalogEquiposView,EliminarEquipoView,EditarEquipoView,ClienteFormView,ObtenerClientesView,GuardarVentaView
from users.views import login_request
from appventas import views
urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('nosotros/', NosotrosView.as_view(), name="Nosotros"),
    path('equipo-form/', EquipoFormView.as_view(), name="EquipoForm"),
    path('list_equipos/', ListEquiposView.as_view(), name="list_equipos"),
    path('catalog_equipos/', CatalogEquiposView.as_view(), name="catalog_equipos"),
    path('eliminar_equipo/<int:equipo_id>/', EliminarEquipoView.as_view(), name="eliminar_equipo"),
    path('editar-equipo/<int:equipo_id>/', EditarEquipoView.as_view(), name='editar_equipo'),
    path('cliente-form/', ClienteFormView.as_view(), name="CLienteForm"),
    path('obtener-clientes/', ObtenerClientesView.as_view(), name='obtener_clientes'),
    path('guardar-venta/', GuardarVentaView.as_view(), name='guardar_venta'),
]

