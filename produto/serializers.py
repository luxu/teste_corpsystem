from rest_framework import serializers

from produto.models import Produto

from categoria.serializers import CategoriaSerializer


class ProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    class Meta:
        model = Produto
        fields = '__all__'

class ProdutoCriarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = (
            'id',
            'categoria',
            'nome',
            'preco',
        )

class ProdutoAtualizarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = (
            'id',
            'categoria',
            'nome',
            'preco',
        )

