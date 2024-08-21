from rest_framework import serializers

from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ClienteCriarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'nome',
        )

class ClienteAtualizarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'nome',
        )

