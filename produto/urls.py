from django.urls import path

from . import api

urlpatterns = [
    path('produtos/', api.produtos),
    path('produto/', api.criar_produto),
    path('produto/<int:id>/', api.atualizar_produto),
    path('produto/<int:id>/deletar_produto/', api.deletar_produto),
]