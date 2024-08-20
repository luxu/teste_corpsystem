from django.db import models

from categoria.models import Categoria


class Produto(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        related_name='produtos',
        on_delete=models.CASCADE
    )
    nome = models.CharField(
        max_length=100
    )
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.categoria.descricao} - {self.nome}'
