from django import forms
from django.forms import ModelForm
from .models import Evento,Direccion,Etiquetas


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = [
            'titulo', 
            'inicio', 
            'fin', 
            'n_max', 
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


