from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Vendedor
from . import serializers


@api_view(['GET'])
def vendedores(request):
    vendas = Vendedor.objects.all()
    serializer = serializers.VendedorSerializer(vendas, many=True)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )

@api_view(['POST'])
def criar_vendedor(request):
    serializer = serializers.VendedorCriarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def atualizar_vendedor(request, id):
    if id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        vendedor = Vendedor.objects.get(id=id)
        serializer = serializers.VendedorAtualizarSerializer(
            vendedor, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Vendedor.DoesNotExist:
        result = Response(
            f"A vendedor com ID:{id} não existe!",
            status=status.HTTP_404_NOT_FOUND
        )
        return result
@api_view(['DELETE'])
def deletar_vendedor(request, id):
    if id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        vendedor = Vendedor.objects.get(id=id)
        vendedor.delete()
        return Response(
            f"A vendedor..: foi deletada com sucesso!",
            status=status.HTTP_204_NO_CONTENT
        )
    except Vendedor.DoesNotExist:
        result = Response(
            f"A vendedor com ID:{id} não existe!",
            status=status.HTTP_404_NOT_FOUND
        )
        return result
