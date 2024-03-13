from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()  
    imagen = models.ImageField(upload_to='appventas/static/assets/img')  
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    correo_electronico = models.EmailField()
    
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    email = models.EmailField()  
    numero_tarjeta = models.CharField(max_length=16)
    fecha_expiracion = models.CharField(max_length=16)

    def __str__(self):
        return f'Venta de {self.cliente.nombre} - Email: {self.email} - Tarjeta: {self.numero_tarjeta}'

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField() 

    def __str__(self):
        return f'Detalle de Venta: {self.venta.id} - Equipo: {self.equipo.nombre} - Cantidad: {self.cantidad}'
 




    
