from django.urls import path

from . import api

urlpatterns = [
    path('vendas/', api.vendas),
    path('listar_vendas/', api.listar_vendas),
    path('vendas_efetuadas_excel/', api.vendas_efetuadas_excel),
    path('vendas_efetuadas_pdf/', api.vendas_efetuadas_pdf),
    path('venda/', api.criar_venda),
    path('venda/<int:id>/', api.atualizar_venda),
    path('venda/deletar_venda/<int:id>/', api.deletar_venda),
]