# Generated by Django 2.2.5 on 2019-10-15 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eventos', '0002_auto_20191015_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direccion',
            name='id',
        ),
        migrations.AlterField(
            model_name='direccion',
            name='calle',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
