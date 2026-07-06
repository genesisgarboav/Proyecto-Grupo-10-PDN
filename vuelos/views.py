# Create your views here.
from django.shortcuts import render, redirect
from .models import Reserva, Vuelo
from .forms import ReservaForm
from django.contrib import messages


#Listar y filtrar registros por vuelos
def lista_reservas(request):
    # El navegador toma lo buscado por el usuario y lo añade al final de la URL como un parámetro
    texto_buscado = request.GET.get('buscar', '')

    if texto_buscado != '':
        vuelos_visibles = Vuelo.objects.filter(destino__icontains=texto_buscado) #Si buscamos algo, filtramos los VUELOS por su destino
    else:
        vuelos_visibles = Vuelo.objects.all() #Si el buscador esta vacío, salen todos los vuelos

    return render(request, 'reservas/lista.html', {'reservas': vuelos_visibles, 'busqueda': texto_buscado}) #Muestra la página web lo datos encontrados


#Función: Crear una nueva reserva
def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)

        if form.is_valid():
            nueva_reserva = form.save()

            #Si se hace una reserva se actualiza el número de asientos disponibles
            vuelo = nueva_reserva.vuelo
            vuelo.asientos = vuelo.asientos - 1
            vuelo.save()
            messages.success(request, "¡Reserva creada con éxito!")
            return redirect('lista_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/form.html', {'form': form, 'titulo': 'Crear Nueva Reserva'})


#Función: Editar una reserva
def editar_reserva(request, pk):
    reserva = Reserva.objects.get(id=pk)

    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            messages.success(request, "Reserva actualizada con éxito.")
            return redirect('lista_reservas')
    else:
        form = ReservaForm(instance=reserva)

    return render(request, 'reservas/form.html', {'form': form, 'titulo': 'Editar Reserva'})


#Función: Eliminar una reserva
def eliminar_reserva(request, pk):
    reserva = Reserva.objects.get(id=pk)

    if request.method == 'POST':
        reserva.vuelo.asientos += 1 #Si se elimina una reserva se devuelve el asiento disponible al vuelo correspondiente
        reserva.vuelo.save()
        reserva.delete()
        messages.success(request, "Reserva eliminada por completo.")
        return redirect('lista_vuelos')

    return render(request, 'reservas/confirm_delete.html', {'reserva': reserva})

#Función: Confirmar pago de reserva
def confirmar_pago(request, pk):
    reserva = Reserva.objects.get(id=pk) # Buscar la reserva por su ID
    reserva.estado = 'Confirmada'
    reserva.save()
    messages.success(request, "Se confirmó el pago del pasajero.")
    return redirect('lista_vuelos')


#Función: Ver (LISTAR) todas las reservas
def ver_reservas(request):
    texto_buscado = request.GET.get('buscar', '')

    if texto_buscado != '':
        todas_las_reservas = Reserva.objects.filter(pasajero_cedula__icontains=texto_buscado).order_by('id') #Se filtra a los usuarios por cédula
    else:
        todas_las_reservas = Reserva.objects.all().order_by('id')

    for indice, reserva in enumerate(todas_las_reservas, start=1):
        reserva.numero_visual = indice

    return render(request, 'reservas/lista_reservas.html', {'reservas': todas_las_reservas, 'busqueda': texto_buscado})