from django.urls import path
from appventas import views
urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('equipos', views.equipos, name="Equipo"),
    path('equipo-form/', views.equipo_form, name="EquipoForm"),
    path('equipo-form2/', views.equipo_form2, name="EquipoForm2"),
    path('buscar', views.buscar, name="Buscar"),
    path('cliente-form/', views.cliente_form, name="CLienteForm"),
]

