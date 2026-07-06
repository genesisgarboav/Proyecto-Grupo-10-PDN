from django import forms
from .models import Reserva

#Utilizamos ModelForm para hacer automáticamente el formulario basado en el modelo de reserva y aplicar reglas de validación
class ReservaForm(forms.ModelForm):
    class Meta: #La clase META le dice django que modelo usar y que campos vamos a mostrar
        model = Reserva
        fields = ['vuelo', 'pasajero_nombre', 'pasajero_cedula', 'estado']

    def clean_vuelo(self):
        vuelo_elegido = self.cleaned_data.get('vuelo') #Tomamos el vuelo que el usuario eligió

        #Valida la disponibilidad de asientos antes de procesar la reserva, si el vuelo existe y NO tiene asientos es 0
        if vuelo_elegido and vuelo_elegido.asientos <= 0:

            self.add_error('vuelo', "Lo sentimos, este vuelo ya no tiene asientos disponibles.") #Al salir este mensaje no se pierden los datos del usuario

        return vuelo_elegido