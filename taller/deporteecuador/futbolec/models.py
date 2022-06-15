from django.db import models

# Create your models here.

class Equipo(models.Model):

    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)
    username = models.CharField(max_length=30)

    def __str__(self):
        return "Nombre Equipo: %s - Siglas: %s - Username: %s" % (self.nombre,
        	self.siglas,
        	self.username)


class Jugador(models.Model):
	nombre = models.CharField("Nombre de estudiante", max_length=30)
	posicion = models.CharField("Posicion de campo", max_length=30)
	nroCamisa = models.IntegerField()
	sueldo = models.IntegerField()
	equipo = models.ForeignKey(Equipo, related_name='losjugadores', on_delete=models.CASCADE)

	def __str__(self):
		return "nombre: %s - posicion: %s - nroCamisa: %d - sueldo: %d - equipo: %s" % (self.nombre, 
        	self.posicion,
            self.nroCamisa,
            self.sueldo,
            self.equipo)


class Campeonato(models.Model):

    nombreC = models.CharField(max_length=200)
    nombreA = models.CharField(max_length=200)

    equipos = models.ManyToManyField(Equipo, through='CampeonatoEquipos')


    def __str__(self):
        return "Nombre Campeonato(%s) - Nombre Auspiciante(%s)" % \
            (self.nombreC, self.nombreA)


class CampeonatoEquipos(models.Model):
	anio = models.IntegerField()
	equipo = models.ForeignKey(Equipo, related_name='loscampeonatos',
		on_delete=models.CASCADE)
	campeonato = models.ForeignKey(Campeonato, related_name='loscampeonatos', 
        on_delete=models.CASCADE)

	def __str__(self):
		return "Año: %d - Equipo: %s - Campeonato: %s" % (self.anio, self.equipo, self.campeonato)
