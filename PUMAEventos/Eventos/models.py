from django.db import models

"""
class EtiquetasWidget(forms.MultiWidget):

    def __init__(self, attrs=None):
        super().__init__([
            forms.TextInput(),
            forms.TextInput()
        ], attrs)
"""
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    #numero maximo de asistentes al evento
    n_max = models.IntegerField()
    descripcion = models.TextField(blank=False, null=False)
    #recinto del evento
    ubicacion = models.CharField(max_length=100)
    #duracion del evento, es valor calculado
    #duracion = self.fin - self.inicio
    
    #periodicidad
    
    class Meta:
        db_table = 'evento'


class Direccion(models.Model):
    evento = models.OneToOneField(
        Evento,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    cp = models.CharField(max_length=100)
    edo = models.CharField(max_length=100)
    colonia = models.CharField(max_length=100)


class Etiquetas(models.Model):
    evento = models.ManyToManyField(Evento)
    etiqueta = models.CharField(max_length=100)

    class Meta:
        db_table = 'etiquetas'



