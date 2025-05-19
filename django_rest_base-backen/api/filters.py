import django_filters
from .models import Mascota

class MascotaFilter(django_filters.FilterSet):
    # Filtros numéricos para edad (rango)
    min_edad = django_filters.NumberFilter(field_name='edad', lookup_expr='gte')
    max_edad = django_filters.NumberFilter(field_name='edad', lookup_expr='lte')

    # Búsqueda parcial en texto para nombre, especie y raza
    nombre = django_filters.CharFilter(field_name='nombre', lookup_expr='icontains')
    especie = django_filters.CharFilter(field_name='especie', lookup_expr='icontains')
    raza = django_filters.CharFilter(field_name='raza', lookup_expr='icontains')

    # Filtro por sexo exacto
    sexo = django_filters.CharFilter(field_name='sexo', lookup_expr='iexact')

    class Meta:
        model = Mascota
        fields = []  # Definidos explícitamente arriba
