from http import HTTPStatus
from fastapi.testclient import TestClient
from fastapi_zero.app import app


#def test_root_deve_retornar_helloworld():
#    """
#   Esse teste tem 3 etapas (AAA)
#   A = Arrange - arranjo
#   A = ACT - Executa a coisa (o SUT)
#   A = Assert - Garanta que A é A
#   """
    #arrange
#   client = TestClient(app)
    #Act
#   response = client.get('/')
    #assert
#   assert response.json() == {'message': 'Olá mundo!'}
#   assert response.status_code == HTTPStatus.OK

def test_exercicio_ola_mundo_em_html():
    client = TestClient(app)

    response = client.get('/api')

    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text