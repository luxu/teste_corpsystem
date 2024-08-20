import json
from datetime import datetime
from http import HTTPStatus
import pytest

from categoria.models import Categoria


def test_categoria(client, db):
    response = client.get('/api/v1/categorias/')
    assert response.status_code == HTTPStatus.OK


def test_criar_categoria(db, client):
    payload = {
        'descricao': 'Alimentos',
    }
    response = client.post('/api/v1/categoria/criar_categoria/', data=payload)
    assert response.status_code == HTTPStatus.CREATED
    resultado = json.loads(response.content)
    assert resultado['descricao'] == payload['descricao']


def test_atualizar_categoria(client, categoria):
    payload = {
        'descricao': 'Alimentos',
    }
    response = client.put(
        f'/api/v1/categoria/{categoria.id}/atualizar_categoria/',
        data=payload,
        content_type="application/json"
    )
    resultado = json.loads(response.content)
    assert resultado['descricao'] == payload['descricao']


def test_deletar_categoria_passar_id_errado(client, categoria):
    id = 2
    url = f'/api/v1/categoria/{id}/deletar_categoria/'
    response = client.delete(url)
    assert response.data == f'A categoria com ID:{id} não existe!'


def test_deletar_categoria(client, categoria):
    url = f'/api/v1/categoria/{categoria.id}/deletar_categoria/'
    response = client.delete(url)
    assert response.status_code == HTTPStatus.NO_CONTENT
