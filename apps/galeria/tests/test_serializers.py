from django.test import TestCase
from galeria.models import Fotografia
from galeria.serializers import FotografiaSerializer, FotografiaSerializerV2, ListaFotografiasPorUsuarioSerializer

class SerializerEstudanteTestCase(TestCase):
    def setUp(self):
        self.fotografia = Fotografia(
            nome="Test Photo",
            legenda="Test Legend",
            categoria="Neptunian",
            descricao="Test Description",
            foto="test_photo.jpg",
            publicada=True,
            usuario=None  # Assuming you have a user instance to assign here
        )
        self.serializer = FotografiaSerializer(instance=self.fotografia)
        self.serializer_v2 = FotografiaSerializerV2(instance=self.fotografia)
        self.lista_serializer = ListaFotografiasPorUsuarioSerializer(instance=self.fotografia)
    
    def test_serializer_fields(self):
        data = self.serializer.data
        self.assertIn('id', data)
        self.assertIn('nome', data)
        self.assertIn('legenda', data)
        self.assertIn('categoria', data)
        self.assertIn('descricao', data)
        self.assertIn('foto', data)
        self.assertIn('publicada', data)
        self.assertIn('data_fotografia', data)