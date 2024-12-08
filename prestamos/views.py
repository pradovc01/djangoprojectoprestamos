from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .models import Interes, Cliente, Prenda, Prestamo, Pago
from .serializers import InteresSerializer, PrendaSerializer, ClienteSerializer, PagoSerializer, PrestamoSerializer
from rest_framework.decorators import api_view

import logging
logger = logging.getLogger(__name__)
# Create your views here.

def index(request):
    return HttpResponse("Hello, world!")

def contact(request, name):
    return HttpResponse(f"Hello {name}")


class InteresViewSet(viewsets.ModelViewSet):
    queryset = Interes.objects.all()
    serializer_class = InteresSerializer

class PrendaViewSet(viewsets.ModelViewSet):
    queryset = Prenda.objects.all()
    serializer_class = PrendaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

# custom API
@api_view(['GET'])
def prestamo_count(request):
    try:
        count = Prestamo.objects.count()
        return JsonResponse({"cantidad": count}, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error":str(e)}, safe=False, status=500)        

@api_view(['GET'])
def prestamo_activos(request):
    try:
        prestamo_activos = Prestamo.objects.filter(activo=True)
        return JsonResponse(PrestamoSerializer(prestamo_activos, many=True).data, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error":str(e)}, safe=False, status=404)        

