from django.contrib import admin
from .models import Mascota

# Registrar el modelo Mascota en el admin sin personalización
admin.site.register(Mascota)
