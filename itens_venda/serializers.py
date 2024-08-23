from rest_framework import serializers

from cliente.models import Cliente
from produto.models import Produto
from vendedor.models import Vendedor
from .models import ItensVenda
from venda.models import Venda


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'


class VendaSerializer(serializers.ModelSerializer):
    vendedor = VendedorSerializer()
    cliente = ClienteSerializer()

    class Meta:
        model = Venda
        fields = (
            'id',
            'total_a_pagar',
            'vendedor',
            'cliente',
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
            'produto',
            'quantidade'
        )


class ItensVendaCriarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensVenda
        fields = (
            'id',
            'venda',
            'produto',
            'quantidade',
        )


class ItensVendaAtualizarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensVenda
        fields = (
            'id',
            'venda',
            'produto',
            'quantidade',
        )
