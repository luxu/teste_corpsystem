from django.urls import path

from . import api

urlpatterns = [
    path('categorias/', api.categorias),
    path('categorias/<int:id>/', api.categoria_por_id),
    path('categoria/', api.criar_categoria),
    path('categoria/<int:id>/', api.atualizar_categoria),
    path('categoria/deletar/<int:id>/', api.deletar_categoria),
]
