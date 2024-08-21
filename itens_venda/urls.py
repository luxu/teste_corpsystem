from django.urls import path

from . import api

urlpatterns = [
    path('itens-vendas/', api.itens_vendas),
    path('itens-venda/', api.criar_itensvendas),
    path('itens-vendas/<int:id>/', api.atualizar_itensvendas),
    path('itens-vendas/deletar/<int:id>/', api.deletar_itensvendas),
]