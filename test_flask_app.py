from app import app
import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index_route(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.data
    assert b'<button id="get_image_btn"' in response.data
    assert b'<img id="random_image"' in response.data
