from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Vendedor

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        # Cria o usuário com a senha de forma segura
        user = User.objects.create_user(**validated_data)
        return user

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'

class VendedorCriarSerializer(serializers.ModelSerializer):
    usuario = UserSerializer()
    class Meta:
        model = Vendedor
        fields = (
            'usuario',
            'nome',
        )

    def create(self, validated_data):
        # Extrai os dados do usuário
        user_data = validated_data.pop('usuario')
        # Cria o usuário
        user = UserSerializer().create(user_data)
        # Cria o vendedor associado ao usuário
        vendedor = Vendedor.objects.create(usuario=user, **validated_data)
        return vendedor

class VendedorAtualizarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = (
            'id',
            'usuario',
            'nome',
        )

