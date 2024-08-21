from django.contrib import admin

from venda.models import Venda

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'vendedor',
        'cliente',
        'total_a_pagar',
        'data_venda',
    )
