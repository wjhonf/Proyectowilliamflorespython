from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()  
    imagen = models.ImageField(upload_to='assets/img/equipos')  
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    correo_electronico = models.EmailField()
    
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1) 
    fecha_venta = models.DateTimeField(auto_now_add=True)


