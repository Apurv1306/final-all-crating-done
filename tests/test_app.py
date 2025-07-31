import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as c:
        yield c

def test_homepage(client):
    rv = client.get('/')
    assert rv.status_code == 200
