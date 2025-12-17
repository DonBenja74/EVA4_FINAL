from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
            'fecha_reserva': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),
            'hora': forms.TimeInput(
                attrs={'type': 'time'}
            ),
        }
