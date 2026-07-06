from django.core.validators import RegexValidator
from django.db import models
# Create your models here.
from django.core.exceptions import ValidationError


# MODELO 1: VUELO
class Vuelo(models.Model):
    ESTADOS_VUELO = [
        ('Programado', 'Programado'),
        ('Abordando', 'Abordando'),
        ('En vuelo', 'En vuelo'),
        ('Aterrizado', 'Aterrizado'),
        ('Cancelado', 'Cancelado'),
    ]

    codigo = models.CharField(max_length=10, unique=True)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha = models.DateField()
    estado = models.CharField(max_length=15, choices=ESTADOS_VUELO, default='Programado')
    asientos = models.IntegerField(help_text="Asientos totales o disponibles")

    def __str__(self):
        return f"{self.codigo} : {self.origen} -> {self.destino} ({self.fecha})"


# MODELO 2: RESERVA
class Reserva(models.Model):
    ESTADOS_RESERVA = [
        ('Pendiente', 'Pendiente de Pago'),
        ('Confirmada', 'Confirmada'),
    ]

    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE, related_name='reservas') #Si se elimina un vuelo, sus reservas también se eliminan
    pasajero_nombre = models.CharField(max_length=150)

    #Validación de la cédula (que solo permite numeros y que sean 10 digitos)
    pasajero_cedula = models.CharField(max_length=10, unique=True, validators=[RegexValidator(regex=r'^\d{10}$', message='La cédula debe tener exactamente números (10).')],
                                       error_messages={'unique': 'Ya existe una reserva registrada con este número de cédula.'})
    #Fecha automatica de la reserva
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=15, choices=ESTADOS_RESERVA, default='Pendiente')

    def __str__(self):
        return f"Reserva {self.id} - {self.pasajero_nombre} ({self.vuelo.codigo})"







