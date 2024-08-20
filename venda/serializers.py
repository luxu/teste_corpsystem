from rest_framework import serializers

from .models import Venda
from categoria.models import Categoria
from itens_venda.models import ItensVenda
from produto.models import Produto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = (
            'id',
            'descricao',
        )

class ProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    class Meta:
        model = Produto
        fields = (
            'id',
            'nome',
            'preco',
            'categoria',
        )

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = (
            'id',
            'venda_numero',
            'total_a_pagar',
            'vendedor',
            'data_venda',
        )

class VendaCriarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = (
            'venda_numero',
            'total_a_pagar',
            'vendedor',
            'data_venda',
        )


class ItensVendaSerializer(serializers.ModelSerializer):
    venda = VendaSerializer(read_only=True)
    produto = ProdutoSerializer(read_only=True)

    class Meta:
        model = ItensVenda
        fields = (
            'id',
            'venda',
            'produto'
        )
