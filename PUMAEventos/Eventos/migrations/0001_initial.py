# Generated by Django 2.2.5 on 2019-10-19 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_de_inicio', models.DateField()),
                ('hora_de_inicio', models.TimeField()),
                ('fecha_final', models.DateField()),
                ('hora_final', models.TimeField()),
                ('cupo_maximo', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('ubicacion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'evento',
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('evento', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Eventos.Evento')),
                ('calle', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=100)),
                ('cp', models.CharField(max_length=100)),
                ('edo', models.CharField(max_length=100)),
                ('colonia', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'direccion',
            },
        ),
        migrations.CreateModel(
            name='Etiquetas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lista', models.CharField(max_length=400)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eventos.Evento')),
            ],
            options={
                'db_table': 'Etiquetas',
            },
        ),
    ]