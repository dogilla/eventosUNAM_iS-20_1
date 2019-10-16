from django import forms
from django.forms import ModelForm
from .models import Evento,Direccion,Etiquetas


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = [
            'titulo',
            'fecha_de_inicio', 
            'hora_de_inicio',
            'fecha_final',
            'hora_final',            
            'cupo_maximo', 
            'descripcion', 
            'ubicacion'
        ]
        
class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = [
            'calle', 
            'numero', 
            'cp', 
            'edo', 
            'colonia'
            ]

class EtiquetasForm(forms.ModelForm):
    class Meta:
        model = Etiquetas
        fields = [
            'etiqueta'
            ]


