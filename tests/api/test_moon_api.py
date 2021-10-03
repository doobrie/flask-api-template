from application.factory import create_app
import pytest
from ..context import application


@pytest.fixture
def client():
    return create_app().test_client()


def test_home_route(client):
    response = client.get('/moon/')
    assert response.get_json() == 'Moon API', 'Route should return "Moon API"'


def test_moon_phase_today(client):
    response = client.get('/moon/phase')
    assert response.status_code == 200, '/moon/phase Invalid status code returned'
    assert float(response.get_json()['phase']) > 0.0, 'Invalid moon phase'
    assert int(response.get_json()['year']) > 0, 'Invalid year'
    assert int(response.get_json()['month']) > 0, 'Invalid month'
    assert int(response.get_json()['day']) > 0, 'Invalid day'


def test_moon_phase(client):
    response = client.get('/moon/phase/2021/9/1')
    assert response.status_code == 200, '/moon/phase/y/m/d Invalid status code returned'
    assert response.get_json()['phase'] == 34.3, 'Invalid moon phase'
    assert response.get_json()['year'] == '2021', 'Invalid year'
    assert response.get_json()['month'] == '9', 'Invalid month'
    assert response.get_json()['day'] == '1', 'Invalid day'


def test_moon_phase_invalid_date(client):
    response = client.get('/moon/phase/2021/9/a')
    assert response.status_code == 400, '/moon/phase/y/m/invalid Invalid status code returned'
