from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse

class AuthenticationUserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_autenticated(self):
        user = authenticate(username='testuser', password='testpassword')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_user_not_authenticated_wrong_password(self):
        user = authenticate(username='testuser', password='wrongpassword')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_user_not_authenticated_wrong_username(self):
        user = authenticate(username='wronguser', password='testpassword')
        self.assertFalse((user is not None) and user.is_authenticated)