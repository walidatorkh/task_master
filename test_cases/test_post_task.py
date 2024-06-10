import pytest
from utils.request_utils import post_request
from data.test_data import create_task_payload, url


@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json",
        "Authorization": "Bearer <your_access_token>"
    }


def test_create_task_success(headers):
    response = post_request(url, headers, create_task_payload)
    assert response.status_code == 200
    assert response.json()["title"] == create_task_payload["title"]


def test_create_task_missing_fields(headers):
    payload = {"title": ""}
    response = post_request(url, headers, payload)
    assert response.status_code == 400
    assert "error" in response.json()


def test_create_task_internal_server_error(headers, mocker):
    mocker.patch("requests.post",
                 return_value=mocker.Mock(status_code=500, json=lambda: {"error": "Internal Server Error"}))
    response = post_request(url, headers, create_task_payload)
    assert response.status_code == 500
    assert "error" in response.json()
