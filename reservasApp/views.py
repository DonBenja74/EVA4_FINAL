from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm
from rest_framework import generics
from .serializers import ReservaSerializer


def listar_reservas(request):
    reservas = Reserva.objects.all().order_by('fecha_reserva')
    return render(request, 'reservas/listar.html', {'reservas': reservas})

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_reservas')
    else:
        form = ReservaForm()

    return render(request, 'reservas/crear.html', {'form': form})

def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)

    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('listar_reservas')
    else:
        form = ReservaForm(instance=reserva)

    return render(request, 'reservas/editar.html', {'form': form})

def eliminar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)

    if request.method == 'POST':
        reserva.delete()
        return redirect('listar_reservas')

    return render(request, 'reservas/eliminar.html', {'reserva': reserva})

class ReservaListCreateAPI(generics.ListCreateAPIView):
    queryset = Reserva.objects.all().order_by('fecha_reserva')
    serializer_class = ReservaSerializer

class ReservaDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

