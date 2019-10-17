from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_de_inicio = models.DateField()
    hora_de_inicio = models.TimeField()
    fechas_final = models.DateField()
    hora_final = models.TimeField()
    #numero maximo de asistentes al evento
    cupo_maximo = models.IntegerField()
    descripcion = models.TextField(blank=False, null=False)
    #recinto del evento
    ubicacion = models.CharField(max_length=100, null=False)
    #duracion del evento, es valor calculado
    duracion = self.hora_final - self.hora_de_inicio
    
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




