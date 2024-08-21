from django.urls import path

from . import api

urlpatterns = [
    path('clientes/', api.clientes),
    path('cliente/', api.criar_cliente),
    path('cliente/<int:id>/', api.atualizar_cliente),
    path('cliente/deletar_cliente/<int:id>/', api.deletar_cliente),
]