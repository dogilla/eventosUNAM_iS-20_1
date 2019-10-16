from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from .models import Evento
from .forms import EventoForm, DireccionForm,EtiquetasForm

"""
detalle del evento
"""
def evento_detail(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    context = {
        'evento': evento
    }
    return render(request, 'Eventos/detalle_evento.html', context)

def evento_view(request):
    if request.method == "POST":
        evento_form = EventoForm(request.POST)
        direccion_form = DireccionForm(request.POST)
        etiquetas_form = EtiquetasForm(request.POST)
        if evento_form.is_valid() and direccion_form.is_valid() and etiquetas_form.is_valid():
            n_evento = evento_form.save()
            n_direccion = direccion_form.save()
            n_etiqueta = etiquetas_form.save()
            return redirect('evento_detail',pk=n_evento.id)
    else:
        evento_form = EventoForm()
        direccion_form = DireccionForm()
        etiquetas_form = EtiquetasForm()
        #contexto para el template
    context = {
        'evento': evento_form,
        'direccion': direccion_form,
        'etiquetas': etiquetas_form
    }
    return render(request,"Eventos/evento.html",context)

def evento_edit(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == "POST":
        evento_form = EventoForm(request.POST, instance=evento)
        direccion_form = DireccionForm(request.POST)
        etiquetas_form = EtiquetasForm(request.POST)
        if evento_form.is_valid() and direccion_form.is_valid() and etiquetas_form.is_valid():
            n_evento = evento_form.save()
            n_direccion = direccion_form.save()
            n_etiqueta = etiquetas_form.save()
            return redirect('evento_detail',pk=n_evento.id)
    else:
        evento_form = EventoForm(instance=evento)
        direccion_form = DireccionForm()
        etiquetas_form = EtiquetasForm()
        #contexto para el template
    context = {
        'evento': evento_form,
        'direccion': direccion_form,
        'etiquetas': etiquetas_form
    }
    return render(request,"Eventos/evento.html",context)
