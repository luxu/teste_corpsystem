from django.urls import path

from . import api

urlpatterns = [
    path('vendas/', api.vendas, name='vendas'),
    path('vendas/criar_venda/', api.criar_venda, name='criar_venda'),
    path('itens-vendas/', api.itens_vendas, name='itens_vendas'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]