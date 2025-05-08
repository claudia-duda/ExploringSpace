from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class AuthenticationUserTestCase(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('Fotografias-list')

    def test_request_without_authentication(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)

    def test_request_with_authentication(self):
        self.client.force_authenticate(self.usuario)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

