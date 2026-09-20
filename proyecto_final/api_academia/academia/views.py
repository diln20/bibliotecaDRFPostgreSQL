from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .models import Programa, Estudiante
from .serializers import ProgramaSerializer, EstudianteSerializer

class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            classes = [AllowAny]
        elif self.action == 'destroy':
            classes = [IsAdminUser]
        else:
            classes = [IsAuthenticated]
        return [permission() for permission in classes]


class EstudianteViewSet(viewsets.ModelViewSet):
    serializer_class = EstudianteSerializer

    def get_queryset(self):
        qs = Estudiante.objects.select_related('programa').all()
        activo = self.request.query_params.get('activo')
        programa = self.request.query_params.get('programa')
        nombre = self.request.query_params.get('nombre')

        if activo in {'true', 'false'}:
            qs = qs.filter(activo=(activo == 'true'))
        if programa:
            qs = qs.filter(programa_id=programa)
        if nombre:
            qs = qs.filter(nombre__icontains=nombre)
        return qs

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            classes = [AllowAny]
        elif self.action == 'destroy':
            classes = [IsAdminUser]
        else:
            classes = [IsAuthenticated]
        return [permission() for permission in classes]
