from rest_framework import serializers

from .models import ItensVenda


class ItensVendaSerializer(serializers.ModelSerializer):
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

