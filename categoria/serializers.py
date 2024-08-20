from rest_framework import serializers

from categoria.models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = (
            'id',
            'descricao',
        )

class CategoriaCriarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = (
            'descricao',
        )

class CategoriaAtualizarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = (
            'descricao',
        )

