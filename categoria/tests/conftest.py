import pytest

from categoria.models import Categoria


@pytest.fixture
def data_categoria():
    return {
        'descricao': 'Camisetas',
    }

@pytest.fixture
def categoria(db, data_categoria):
    return Categoria.objects.create(**data_categoria)
