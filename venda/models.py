from django.db import models

from cliente.models import Cliente
from vendedor.models import Vendedor


class Venda(models.Model):
    vendedor = models.ForeignKey(
        Vendedor,
        related_name='vendedor_venda',
        on_delete=models.CASCADE
    )
    cliente = models.ForeignKey(
        Cliente,
        related_name='cliente_venda',
        on_delete=models.CASCADE
    )
    total_a_pagar = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True, blank=True
    )
    data_venda = models.DateTimeField()

    def __str__(self):
        return f'{self.id} - {self.data_venda}'
