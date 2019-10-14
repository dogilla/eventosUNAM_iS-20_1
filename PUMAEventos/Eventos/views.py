from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Evento
from .forms import EventoForm, DireccionForm, EtiquetasForm


def evento_view(request):
    evento_form = EventoForm(request.POST or None)
    direccion_form = DireccionForm(request.POST or None)
    etiquetas_form = EtiquetasForm(request.POST or None)
    if evento_form.is_valid() and direccion_form.is_valid() and etiquetas_form.is_valid():
        evento_form.save()
        direccion_form.save()
        etiquetas_form.save()
    #contexto para el template
    context = {
        'evento': evento_form,
        'direccion': direccion_form,
        'etiquetas': etiquetas_form
    }
    return render(request,"Eventos/evento.html",context)

