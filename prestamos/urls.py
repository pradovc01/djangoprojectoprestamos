from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'interes', views.InteresViewSet)
router.register(r'prenda', views.PrendaViewSet)
router.register(r'cliente', views.ClienteViewSet)
router.register(r'prestamo', views.PrestamoViewSet)
router.register(r'pago', views.PagoViewSet)



urlpatterns = [    
    path('', include(router.urls)),
    path('prestamo/count', views.prestamo_count, name='prestamo-count'),
    path('prestamo/activos', views.prestamo_activos, name='prestamo-activos'),
]