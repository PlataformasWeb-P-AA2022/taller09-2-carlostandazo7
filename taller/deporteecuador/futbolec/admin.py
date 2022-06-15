from django.contrib import admin

# Register your models here.


# Importar las clases del modelo
from futbolec.models import Equipo, Jugador, Campeonato, CampeonatoEquipos

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Estudiante
class EquipoAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ('nombre', 'siglas', 'username')
    search_fields = ('nombre', 'siglas')
# admin.site.register se lo altera
# el primer argumento es el modelo (Estudiante)
# el segundo argumento la clase EstudianteAdmin
admin.site.register(Equipo, EquipoAdmin)

# admin.site.register(Matricula)
class JugadorAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ('nombre', 'posicion', 'nroCamisa', 'sueldo','equipo')
    search_fields = ('equipo__nombre',)

admin.site.register(Jugador, JugadorAdmin)

class CampeonatoAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ('nombreC', 'nombreA')
    search_fields = ('nombreC', 'nombreA',)

admin.site.register(Campeonato, CampeonatoAdmin)

class CampeonatoEAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ('anio', 'equipo', 'campeonato')
    search_fields = ('equipo__nombre', 'campeonato__nombreC',)

admin.site.register(CampeonatoEquipos, CampeonatoEAdmin)


