import json
from http import HTTPStatus


def test_categoria(client, categoria):
    url = '/api/v1/categorias/'
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) >= 0


def test_categoria_por_id_errado(client, categoria):
    url = '/api/v1/categorias/2/'
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 0


def test_categoria_por_id(client, categoria):
    url = f'/api/v1/categorias/{categoria.id}/'
    response = client.get(url)
    resultado = json.loads(response.content)[0]
    assert resultado['descricao'] == 'Camisetas'


def test_criar_categoria_sem_parametros(db, client):
    url = '/api/v1/categoria/'
    response = client.post(url)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    resultado = json.loads(response.content)
    assert resultado['descricao'] == ['Este campo é obrigatório.']


def test_criar_categoria(db, client):
    url = '/api/v1/categoria/'
    payload = {
        'descricao': 'Alimentos',
    }
    response = client.post(url, data=payload)
    assert response.status_code == HTTPStatus.CREATED
    resultado = json.loads(response.content)
    assert resultado['descricao'] == payload['descricao']


def test_atualizar_categoria_id_errado(client, categoria):
    url = f'/api/v1/categorias/{categoria.id}/'
    response = client.get(url)
    resultado = json.loads(response.content)[0]
    assert resultado['descricao'] == 'Camisetas'
    payload = {
        'descricao': 'Camisetas/Calças',
    }
    categoria_id = 3
    url = f'/api/v1/categoria/{categoria_id}/'
    response = client.put(
        url,
        data=payload,
        content_type="application/json"
    )
    assert response.data == f"A categoria com ID:{categoria_id} não existe!"

def test_atualizar_categoria(client, categoria):
    url = f'/api/v1/categorias/{categoria.id}/'
    response = client.get(url)
    resultado = json.loads(response.content)[0]
    assert resultado['descricao'] == 'Camisetas'
    payload = {
        'descricao': 'Camisetas/Calças',
    }
    response = client.put(
        f'/api/v1/categoria/{categoria.id}/',
        data=payload,
        content_type="application/json"
    )
    assert response.data['descricao'] == payload['descricao']


def test_deletar_categoria_passar_id_errado(client, categoria):
    id = 2
    url = f'/api/v1/categoria/deletar/{id}/'
    response = client.delete(url)
    assert response.data == f'A categoria com ID:{id} não existe!'


def test_deletar_categoria(client, categoria):
    url = f'/api/v1/categoria/deletar/{categoria.id}/'
    response = client.delete(url)
    assert response.status_code == HTTPStatus.NO_CONTENT
    assert response.data == f'A categoria..:{categoria.descricao} foi deletada com sucesso!'
