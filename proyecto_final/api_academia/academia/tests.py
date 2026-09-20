from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Programa

class ProgramaApiTests(APITestCase):
    def setUp(self):
        self.programa = Programa.objects.create(codigo='SIS', nombre='Sistemas')
        self.user = get_user_model().objects.create_user(username='docente', password='clave-segura-123')

    def test_listar_programas(self):
        response = self.client.get('/api/programas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_crear_estudiante_requiere_autenticacion(self):
        response = self.client.post('/api/estudiantes/', {
            'nombre': 'Ana Torres',
            'correo': 'ana@example.com',
            'programa': self.programa.id,
        }, format='json')
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_crear_estudiante_autenticado(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/estudiantes/', {
            'nombre': 'Ana Torres',
            'correo': 'ana@example.com',
            'programa': self.programa.id,
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
