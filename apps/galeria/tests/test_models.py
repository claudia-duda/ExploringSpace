from django.test import TestCase
from galeria.models import Fotografia

class ModelFotografiaTestCase(TestCase):
    def setUp(self):
        Fotografia.objects.create(
            nome="Test Photo",
            legenda="Test Legend",
            categoria="Neptunian",
            descricao="Test Description",
            foto="test_photo.jpg",
            publicada=True,
            usuario=None  # Assuming you have a user instance to assign here
        )

    def test_fotografia_creation(self):
        photo = Fotografia.objects.get(nome="Test Photo")
        self.assertEqual(photo.legenda, "Test Legend")
        self.assertEqual(photo.categoria, "Neptunian")
        self.assertEqual(photo.descricao, "Test Description")
        self.assertTrue(photo.publicada)
        self.assertIsNotNone(photo.foto)