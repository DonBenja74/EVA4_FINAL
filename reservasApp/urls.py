from django.urls import path
from .views import (listar_reservas,crear_reserva,editar_reserva,eliminar_reserva,ReservaListCreateAPI,ReservaDetailAPI)

urlpatterns = [
    path('reservas/', listar_reservas, name='listar_reservas'),
    path('reservas/nueva/', crear_reserva, name='crear_reserva'),
    path('reservas/editar/<int:id>/', editar_reserva, name='editar_reserva'),
    path('reservas/eliminar/<int:id>/', eliminar_reserva, name='eliminar_reserva'),

    path('api/reservas/', ReservaListCreateAPI.as_view(), name='api_reservas'),
    path('api/reservas/<int:pk>/', ReservaDetailAPI.as_view(), name='api_reserva_detalle'),
]
