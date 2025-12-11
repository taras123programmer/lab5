import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, world!"}


def test_add(client):
    response = client.get('/add/2/3')
    assert response.status_code == 200
    assert response.json == {"result": 5}
