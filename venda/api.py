from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from itens_venda.models import ItensVenda
from .models import Venda
from .serializers import VendaSerializer, ItensVendaSerializer, VendaCriarSerializer


@api_view(['GET'])
def vendas(request):
    vendas = Venda.objects.all()
    serializer = VendaSerializer(vendas, many=True)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )

@api_view(['POST'])
def criar_venda(request):
    serializer = VendaCriarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def itens_vendas(request):
    itens_vendas = ItensVenda.objects.all()
    serializer = ItensVendaSerializer(itens_vendas, many=True)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )

