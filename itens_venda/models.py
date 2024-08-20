from django.db import models

from produto.models import Produto
from venda.models import Venda


class ItensVenda(models.Model):
    venda = models.ForeignKey(
        Venda,
        related_name='vendas',
        on_delete=models.CASCADE
    )
    produto = models.ForeignKey(
        Produto,
        related_name='produtos',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.venda} - {self.produto}'
