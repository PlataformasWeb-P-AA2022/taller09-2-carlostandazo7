# Generated by Django 4.0.5 on 2022-06-15 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreC', models.CharField(max_length=200)),
                ('nombreA', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('siglas', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre de estudiante')),
                ('posicion', models.CharField(max_length=30, verbose_name='Posicion de campo')),
                ('nroCamisa', models.IntegerField()),
                ('sueldo', models.IntegerField()),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='losjugadores', to='futbolec.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='CampeonatoEquipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField()),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loscampeonatos', to='futbolec.campeonato')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loscampeonatos', to='futbolec.equipo')),
            ],
        ),
        migrations.AddField(
            model_name='campeonato',
            name='equipos',
            field=models.ManyToManyField(through='futbolec.CampeonatoEquipos', to='futbolec.equipo'),
        ),
    ]