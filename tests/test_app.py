from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fastapi_zero.app import app


@pytest.fixture
def client():
    return TestClient(app)


# def test_root_deve_retornar_helloworld():
#    """
#   Esse teste tem 3 etapas (AAA)
#   A = Arrange - arranjo
#   A = ACT - Executa a coisa (o SUT)
#   A = Assert - Garanta que A é A
#   """
# arrange
#   client = TestClient(app)
# Act
#   response = client.get('/')
# assert
#   assert response.json() == {'message': 'Olá mundo!'}
#   assert response.status_code == HTTPStatus.OK


def test_created_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'email': 'bob@example.com',
        'username': 'bob',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'bob',
                'email': 'bob@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
