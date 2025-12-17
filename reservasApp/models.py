from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Reserva(models.Model):

    ESTADOS = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO ASISTEN', 'No asisten'),
    ]

    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha_reserva = models.DateField()
    hora = models.TimeField()
    cantidad_personas = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(15)]
    )
    estado = models.CharField(max_length=20, choices=ESTADOS)
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha_reserva}"
