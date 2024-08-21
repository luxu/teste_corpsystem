from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Categoria
from . import serializers


@api_view(['GET'])
def categorias(request):
    vendas = Categoria.objects.all()
    serializer = serializers.CategoriaSerializer(vendas, many=True)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def criar_categoria(request):
    serializer = serializers.CategoriaCriarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def atualizar_categoria(request, id):
    if id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        categoria = Categoria.objects.get(id=id)
        serializer = serializers.CategoriaAtualizarSerializer(
            categoria, data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Categoria.DoesNotExist:
        result = Response(
            f"A categoria com ID:{id} não existe!",
            status=status.HTTP_404_NOT_FOUND
        )
        return result


@api_view(['DELETE'])
def deletar_categoria(request, id):
    if id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        categoria = Categoria.objects.get(id=id)
        categoria.delete()
        return Response(
            f"A categoria..:{categoria.descricao} foi deletada com sucesso!",
            status=status.HTTP_204_NO_CONTENT
        )
    except Categoria.DoesNotExist:
        result = Response(
            f"A categoria com ID:{id} não existe!",
            status=status.HTTP_404_NOT_FOUND
        )
        return result
