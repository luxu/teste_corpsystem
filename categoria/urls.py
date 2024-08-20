from django.urls import path

from . import api

urlpatterns = [
    path('categorias/', api.categorias, name='categorias'),
    path('categoria/criar_categoria/', api.criar_categoria, name='criar_categoria'),
    path('categoria/<int:id>/atualizar_categoria/', api.atualizar_categoria, name='atualizar_categoria'),
    path('categoria/<int:id>/deletar_categoria/', api.deletar_categoria, name='deletar_categoria'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]