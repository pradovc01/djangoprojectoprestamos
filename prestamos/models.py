from django.db import models
from .validators import validar_positivos, validar_string

# Create your models here.
class Interes(models.Model):
    rango_inicial = models.IntegerField(null=True, validators=[validar_positivos])
    rango_final = models.IntegerField(null = True, validators=[validar_positivos])
    tasa = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.tasa} %'
    
    class Meta:
        verbose_name = 'Interes'
        verbose_name_plural = 'Interes'
        db_table='interes'
        ordering=['id','rango_inicial']

class TipoPrenda(models.TextChoices):
    JOYA = 'JO', 'Joya'
    MOVILIDAD = 'MO', 'Movilidad'
    MOTOCICLETA = 'MOT', 'Motocicleta'

class TipoPago(models.TextChoices):
    INTERES = 'IN', 'Interes'
    PAGO = 'PA', 'Pago'

class Prenda(models.Model):   
    descripcion = models.CharField(max_length=200)
    categoria = models.CharField(max_length=3, choices=TipoPrenda.choices, default=TipoPrenda.JOYA)    

    def __str__(self):
        return f'{self.categoria}: {self.descripcion}'
    class Meta:
        verbose_name = 'Prenda'
        verbose_name_plural = 'Prendas'
        db_table='prenda'
        ordering=['id']

class Cliente(models.Model):
    nombres = models.CharField(max_length=30, validators=[validar_string])
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    ci = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    nota = models.TextField
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now_add=True)
    direccion = models.CharField(max_length=200)

    def nombre_completo(self):
        return f'{self.apellido_paterno} {self.apellido_materno}, {self.nombres}'

    def __str__(self):
        return self.nombre_completo()
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table='cliente'
        ordering=['id']

class Prestamo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    prenda = models.ForeignKey(Prenda, on_delete=models.CASCADE)
    numero_factura = models.CharField(max_length=30)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_fin_prestamo = models.DateField
    capital =  models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_positivos])
    interes = models.ForeignKey(Interes, on_delete=models.CASCADE)
    descripcion = models.TextField
    activo =models.BooleanField(default=True)
    numero_cuotas = models.IntegerField(null = True, validators=[validar_positivos])
    
    def __str__(self):
        return f'{self.cliente.nombre_completo()}: {self.prenda.descripcion}'
    
    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'
        db_table='prestamo'
        ordering=['id']

class Pago(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    fecha_pago = models.DateField(auto_now_add=True)
    monto = models.DecimalField(max_digits=5, decimal_places=2)
    numero_pago = models.IntegerField(null = True, validators=[validar_positivos])
    tipo_pago = models.CharField(max_length=2, choices=TipoPago.choices, default=TipoPago.INTERES)
    
    def __str__(self):
        return f'{self.prestamo.cliente.nombre_completo()}: {self.prestamo.prenda.descripcion}:Fact {self.prestamo.numero_factura} - Capital:{self.prestamo.capital}'
    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        db_table='pago'
        ordering=['id']

