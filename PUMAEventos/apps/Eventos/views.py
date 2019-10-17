from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from apps.Eventos.models import Evento
from apps.Eventos.forms import EventoForm, DireccionForm,EtiquetasForm

def index(request):
    return HttpResponse("Index")

def evento_view(request):
    if request.method == "POST":
        evento_form = EventoForm(request.POST)
        if evento_form.is_valid():
            evento_form.save()
        return redirect('evento:evento_lista')
    return render(request,"Eventos/eventosform.html",{'eventosform':evento_form})


def evento_edit(request, pk):
    evento = Evento.objects.get(pk=pk) 
    if request.method == "GET":
        evento_form = EventoForm(instance=evento)
    else:
        evento_form = EventoForm(request.POST, instance=evento)
        if evento_form.is_valid():
            evento_form.save()
        return redirect('evento: evento_lista')
    return render(request, 'Eventos/eventosform.html', {'eventosform': evento_form})

def evento_delete(request, pk):
    evento = Evento.objects.get(pk=pk) 
    if request.method == 'POST':
        evento.delete()
        return redirect('evento: evento_lista')
    return render(request, 'Eventos/evento_delete.html', {'evento': evento})


def evento_lista(request):
    context={}
    all_eventos = Evento.objects.all().order_by('pk')   
    context['eventos'] = all_eventos
    return render (request, 'Eventos/evento_lista.html', context)

class EventoList(ListView):
    model = Evento
    template_name = 'Eventos/evento_lista.html'    

class EventoCreate(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'Eventos/eventosform.html'
    success_url = reverse_lazy('Eventos/evento_lista')

class EventoUpdate(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'Eventos/eventosform.html'
    success_url = reverse_lazy('Eventos/evento_lista')

class EventoDelete(DeleteView):
    model = Evento
    template_name = 'Eventos/evento_delete.html'
    success_url = reverse_lazy('Eventos/evento_lista')


