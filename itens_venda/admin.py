from django.contrib import admin

from .models import ItensVenda

@admin.register(ItensVenda)
class ItensVendaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'venda',
        'produto',
    )
