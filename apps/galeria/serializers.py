from rest_framework import serializers

from apps.galeria.models import Fotografia


class FotografiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotografia
        fields = ['id', 'nome', 'categoria', 'descricao', 'foto','legenda']