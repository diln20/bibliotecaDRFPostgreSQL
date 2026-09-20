from rest_framework import serializers
from .models import Programa, Estudiante

class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = ['id', 'codigo', 'nombre', 'activo']


class EstudianteSerializer(serializers.ModelSerializer):
    programa_nombre = serializers.CharField(source='programa.nombre', read_only=True)
    estado_texto = serializers.SerializerMethodField()

    class Meta:
        model = Estudiante
        fields = [
            'id',
            'nombre',
            'correo',
            'activo',
            'estado_texto',
            'fecha_creacion',
            'programa',
            'programa_nombre',
        ]
        read_only_fields = ['id', 'fecha_creacion']

    def get_estado_texto(self, obj):
        return 'Activo' if obj.activo else 'Inactivo'

    def validate_nombre(self, value):
        value = value.strip()
        if len(value) < 3:
            raise serializers.ValidationError('El nombre debe tener al menos 3 caracteres.')
        return value
