from application.factory import create_app
import pytest
from ..context import application


@pytest.fixture
def client():
    return create_app().test_client()


def test_home_route(client):
    response = client.get('/sun/')
    assert response.get_json() == 'Sun API', 'Route should return "Sun API"'


def test_equinox(client):
    response = client.get('/sun/equinox')
    assert response.status_code == 200, 'Invalid status code returned'
    assert len(response.get_json()["equinox"]
               ) > 0, 'Equinox json was not retrieved'

    assert len(response.get_json()["autumnal_equinox"]
               ) > 0, 'Autumnal Equinox json was not retrieved'

    assert len(response.get_json()["summer_solstice"]
               ) > 0, 'Summer Solstice json was not retrieved'

    assert len(response.get_json()["winter_solstice"]
               ) > 0, 'Winter Solstice json was not retrieved'
