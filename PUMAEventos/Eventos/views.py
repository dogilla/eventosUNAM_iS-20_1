from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Evento
from .forms import EventoForm, DireccionForm,EtiquetasForm


def evento_view(request):
    if request.method == "POST":
        evento_form = EventoForm(request.POST)
        direccion_form = DireccionForm(request.POST)
        etiquetas_form = EtiquetasForm(request.POST)
        if evento_form.is_valid() and direccion_form.is_valid() and etiquetas_form.is_valid():
            n_evento = evento_form.save(commit=False)
            n_direccion = direccion_form.save(commit=False)
            n_etiqueta = etiquetas_form.save(commit=False)
            return redirect('detalle_evento', pk=n_evento.pk)
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

"""
def evento_edit(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == "POST":
        evento_form = EventoForm(request.POST, instance=post)
        if evento_form.is_valid():
            evento = evento_form.save()
            return redirect('detalle_evento', pk=evento.pk)
        else:
            evento_form = EventoForm(instance=post)
        return render(request, 'Evento/evento_edit.html', {'evento': evento_form})
"""