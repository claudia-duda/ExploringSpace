from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse

class FotografiasTestCase(TestCase):
    
    def setUp(self):
        self.usuario = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('Fotografias-list')
        self.client.force_authenticate(self.usuario)
        self.fotografia = {
            'nome': 'Test Photo',
            'legenda': 'Test Legend',
            'categoria': 'Neptunian',
            'descricao': 'Test Description',
            'foto': 'test_photo.jpg',
            'publicada': True,
            'usuario': self.usuario.id
        }
        self.fotografia2 = {
            'nome': 'Test Photo 2',
            'legenda': 'Test Legend 2',
            'categoria': 'Neptunian',
            'descricao': 'Test Description 2',
            'foto': 'test_photo_2.jpg',
            'publicada': True,
            'usuario': self.usuario.id
        }

    def test_request_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)