from django.contrib import admin

from categoria.models import Categoria


@admin.register(Categoria)
class ModelNameAdmin(admin.ModelAdmin):
    ...
