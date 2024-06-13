from app import app
import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_image_route(client):
    response = client.get("/get_image")

    assert response.status_code == 200
    assert response.content_type == "image/jpeg" or "image/png"
