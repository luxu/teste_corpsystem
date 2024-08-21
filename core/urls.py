
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('categoria.urls')),
    path('api/v1/', include('cliente.urls')),
    path('api/v1/', include('produto.urls')),
    path('api/v1/', include('vendedor.urls')),
    path('api/v1/', include('venda.urls')),
    path('api/v1/', include('itens_venda.urls')),
]
