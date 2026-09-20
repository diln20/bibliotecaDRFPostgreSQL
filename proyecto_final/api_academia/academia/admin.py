from django.contrib import admin
from .models import Programa, Estudiante

@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre', 'activo')
    list_filter = ('activo',)
    search_fields = ('codigo', 'nombre')

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'correo', 'programa', 'activo', 'fecha_creacion')
    list_filter = ('activo', 'programa')
    search_fields = ('nombre', 'correo')
