"""
URL configuration for aerolinea_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vuelos import views

urlpatterns = [
    # 1. El panel de administración de Django
    path('admin/', admin.site.urls),
    path('vuelos', views.lista_reservas, name='lista_vuelos'), #Ruta principal: Muestra la tabla de reservas, vuelos disponibles y el buscador
    path('reservas/', views.ver_reservas, name='lista_reservas'),
    path('nueva/', views.crear_reserva, name='crear_reserva'),   #Ruta para el formulario de crear nueva reserva
    path('editar/<int:pk>/', views.editar_reserva, name='editar_reserva'), #Ruta para editar una reserva usando su ID
    path('eliminar/<int:pk>/', views.eliminar_reserva, name='eliminar_reserva'), #Ruta para eliminar una reserva usando su ID
    path('confirmar/<int:pk>/', views.confirmar_pago, name='confirmar_pago'), #Botón para confirmar el pago de la reserva
]