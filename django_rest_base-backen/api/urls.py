from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MascotaViewSet, RegisterView

router = DefaultRouter()
router.register(r'mascotas', MascotaViewSet, basename='mascota')

urlpatterns = [
    path('', include(router.urls)),                      # CRUD completo para Mascota
    path('register/', RegisterView.as_view(), name='register'),  # Registro de usuarios
]
