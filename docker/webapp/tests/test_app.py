from web.app import create_app
import pytest
import sys
import os
base_dir = os.path.dirname(__file__)
webapp_path = os.path.join(base_dir, '..', 'webapp')
abs_webapp_path = os.path.abspath(webapp_path)
sys.path.insert(0, abs_webapp_path)


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_app_route(client):
    """Verifica que la ruta /app responde con el texto esperado."""
    response = client.get('/app')
    assert response.status_code == 200
    assert b'This is the app route!' in response.data
