"""PUMAEventos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from apps.Eventos.views import evento_view, evento_lista, evento_edit, \
    EventoCreate, EventoList, EventoUpdate
# , evento_lista, evento_delete, evento_edit, \
 #   EventoList, EventoCreate, EventoUpdate, EventoDelete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^', include('PUMAEventos.apps.Eventos.urls'))
    #path('evento/', evento_view),
    path('nuevo/', EventoCreate.as_view(), name='evento_crear'),
    path('editar/<int:pk>', EventoUpdate.as_view(), name='evento_edit'),
    #path('eliminar/<int:pk>/', EventoDelete.as_view(), name='evento_delete'),
    path('lista/', EventoList.as_view(), name='evento_lista'),
]

