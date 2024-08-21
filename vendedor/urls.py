from django.urls import path

from . import api

urlpatterns = [
    path('vendedores/', api.vendedores),
    path('vendedor/', api.criar_vendedor),
    path('vendedor/<int:id>/', api.atualizar_vendedor),
    path('vendedor/<int:id>/deletar_vendedor/', api.deletar_vendedor),
]