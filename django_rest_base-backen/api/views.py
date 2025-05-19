from rest_framework import viewsets, filters, generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from .models import Mascota
from .serializers import MascotaSerializer, RegisterSerializer, CustomTokenObtainPairSerializer
from .pagination import CustomPagination
# from .filters import MascotaFilter  # Si deseas usar filtros personalizados

# Vista principal para el modelo Mascota
class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # filterset_class = MascotaFilter  # Descomenta si tienes filtros personalizados

    ordering_fields = ['edad', 'fecha_registro']
    ordering = ['-fecha_registro']

    pagination_class = CustomPagination  # Aquí añades la paginación personalizada

# Vista para registro de usuarios
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

# Vista para autenticación JWT personalizada
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
