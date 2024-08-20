from django.contrib.auth.models import User
from django.db import models


class Vendedor(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    nome = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.nome
