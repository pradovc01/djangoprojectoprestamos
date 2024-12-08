from rest_framework import serializers
from .models import Interes, Prestamo, Prenda, Cliente, Pago

class InteresSerializer(serializers.ModelSerializer):
    class Meta:
        model= Interes
        fields = '__all__'

class PrendaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Prenda
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'