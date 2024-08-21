from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ItensVenda
from . import serializers


@api_view(['GET'])
def itens_vendas(request):
    vendas = ItensVenda.objects.all()
    serializer = serializers.ItensVendaSerializer(vendas, many=True)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )

@api_view(['POST'])
def criar_itensvendas(request):
    serializer = serializers.ItensVendaCriarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def atualizar_itensvendas(request, id):
    if id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        venda = ItensVenda.objects.get(id=id)
        serializer = serializers.ItensVendaAtualizarSerializer(
            venda, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ItensVenda.DoesNotExist:
        result = Response(
            f"A venda com ID:{id} não existe!",
            status=status.HTTP_404_NOT_FOUND
        )
        return result
@api_view(['DELETE'])
def deletar_itensvendas(request, id):
    if id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        venda = ItensVenda.objects.get(id=id)
        venda.delete()
        return Response(
            f"A venda..: foi deletada com sucesso!",
            status=status.HTTP_204_NO_CONTENT
        )
    except ItensVenda.DoesNotExist:
        result = Response(
            f"A venda com ID:{id} não existe!",
            status=status.HTTP_404_NOT_FOUND
        )
        return result
