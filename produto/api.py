from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Produto
from . import serializers


@api_view(['GET'])
def produtos(request):
    produtos = Produto.objects.all()
    serializer = serializers.ProdutoSerializer(produtos, many=True)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )

@api_view(['POST'])
def criar_produto(request):
    serializer = serializers.ProdutoCriarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def atualizar_produto(request, id):
    if id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        produto = Produto.objects.get(id=id)
        serializer = serializers.ProdutoAtualizarSerializer(
            produto, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Produto.DoesNotExist:
        result = Response(
            f"A produto com ID:{id} não existe!",
            status=status.HTTP_404_NOT_FOUND
        )
        return result
@api_view(['DELETE'])
def deletar_produto(request, id):
    if id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        produto = Produto.objects.get(id=id)
        produto.delete()
        return Response(
            f"A produto..: foi deletada com sucesso!",
            status=status.HTTP_204_NO_CONTENT
        )
    except Produto.DoesNotExist:
        result = Response(
            f"A produto com ID:{id} não existe!",
            status=status.HTTP_404_NOT_FOUND
        )
        return result
