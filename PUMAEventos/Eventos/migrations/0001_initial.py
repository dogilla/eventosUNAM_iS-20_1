# Generated by Django 2.2.5 on 2019-11-07 17:57

from django.db import migrations, models


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
                ('entidad', models.CharField(max_length=150)),
                ('correo', models.EmailField(default='null@c.com', max_length=150)),
            ],
            options={
                'db_table': 'evento',
            },
        ),
        migrations.CreateModel(
            name='RegEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_Evento', models.IntegerField()),
                ('email_Organizador', models.EmailField(max_length=254)),
                ('email_Usuario', models.EmailField(max_length=254)),
            ],
            options={
                'unique_together': {('id_Evento', 'email_Usuario')},
            },
        ),
    ]
