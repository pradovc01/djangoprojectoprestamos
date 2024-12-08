from django.contrib import admin
from .models import Interes, Prenda, Cliente, Prestamo, Pago

# Register your models here.



class InteresAdmin(admin.ModelAdmin):
    list_display = ('rango_inicial','rango_final','tasa',)
    ordering = ('rango_inicial',)
    search_fields = ('rango_inicial','rango_final',)
admin.site.register(Interes, InteresAdmin)

class PrestamoInline(admin.TabularInline):
    model = Prestamo

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('apellido_paterno','apellido_materno','nombres', 'ci')
    ordering = ('apellido_paterno','apellido_materno', 'nombres')
    search_fields = ('apellido_paterno','apellido_materno',)
    list_filter=['activo']
    inlines = [PrestamoInline,]
admin.site.register(Cliente, ClienteAdmin)

class PrendaAdmin(admin.ModelAdmin):
    list_display = ('categoria','descripcion')  
    ordering = ['categoria', 'descripcion']
    search_fields = ['descripcion']

admin.site.register(Prenda, PrendaAdmin)

class PagoInline(admin.TabularInline):
    model = Pago


class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('numero_factura','fecha_prestamo', 'cliente', 'prenda','capital','interes')
    ordering = ['fecha_prestamo']
    search_fields = ('numero_factura','cliente','numero_factura',)
    list_filter = ['activo', 'interes']
    inlines = [PagoInline,]

admin.site.register(Prestamo, PrestamoAdmin)


class PagoAdmin(admin.ModelAdmin):
    list_display = ('prestamo','fecha_pago', 'numero_pago', 'tipo_pago','monto')
    ordering = ['fecha_pago']
    search_fields = ('prestamo','fecha_pago','numero_factura',)


admin.site.register(Pago, PagoAdmin)
