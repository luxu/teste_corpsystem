from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cliente
from . import serializers


@api_view(['GET'])
def clientes(request):
    produtos = Cliente.objects.all()
    serializer = serializers.ClienteSerializer(produtos, many=True)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )

@api_view(['POST'])
def criar_cliente(request):
    serializer = serializers.ClienteCriarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def atualizar_cliente(request, id):
    if id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        cliente = Cliente.objects.get(id=id)
        serializer = serializers.ClienteAtualizarSerializer(
            cliente, data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Cliente.DoesNotExist:
        result = Response(
            f"A cliente com ID:{id} não existe!",
            status=status.HTTP_404_NOT_FOUND
        )
        return result
@api_view(['DELETE'])
def deletar_cliente(request, id):
    if id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        cliente = Cliente.objects.get(id=id)
        cliente.delete()
        return Response(
            f"A cliente..: foi deletada com sucesso!",
            status=status.HTTP_204_NO_CONTENT
        )
    except Cliente.DoesNotExist:
        result = Response(
            f"A cliente com ID:{id} não existe!",
            status=status.HTTP_404_NOT_FOUND
        )
        return result
