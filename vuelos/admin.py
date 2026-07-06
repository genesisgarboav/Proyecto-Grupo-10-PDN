# Register your models here.
from django.contrib import admin
from .models import Vuelo, Reserva

# Registramos los modelos
admin.site.register(Vuelo)
admin.site.register(Reserva)