from rest_framework import serializers
from apps.galeria.models import Fotografia


class FotografiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotografia
        fields = ['id', 'nome', 'categoria', 'descricao', 'foto','legenda']

class ListaFotografiasPorUsuarioSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source = 'usuario.username')
    nome_fotografia = serializers.ReadOnlyField(source = 'nome')
    categoria = serializers.SerializerMethodField()
    class Meta:
        model = Fotografia
        fields =  ['usuario', 'nome_fotografia', 'categoria']

    def get_categoria(self, obj):
        return obj.get_categoria_display()

