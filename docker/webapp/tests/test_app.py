import pytest
from web.app import create_app
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_route(client):
    """Verifica que la ruta / responde con el texto esperado."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello World!' in response.data


def test_metrics_route(client):
    """Verifica que la ruta /metrics responde con datos de métricas."""
    response = client.get('/metrics')
    assert response.status_code == 200
    assert b'request_processing_seconds' in response.data
