import pytest
from data.test_data import url
from utils.request_utils import get_request


@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json",
        "Authorization": "Bearer <your_access_token>"
    }


def test_get_task_success(headers):
    task_id = "existing_task_id"
    response = get_request(f"{url}/{task_id}", headers)
    assert response.status_code == 200
    assert "title" in response.json()


def test_get_task_not_found(headers):
    task_id = "non_existent_task_id"
    response = get_request(f"{url}/{task_id}", headers)
    assert response.status_code == 404
    assert "error" in response.json()


def test_get_task_internal_server_error(headers, mocker):
    task_id = "existing_task_id"
    mocker.patch("requests.get",
                 return_value=mocker.Mock(status_code=500, json=lambda: {"error": "Internal Server Error"}))
    response = get_request(f"{url}/{task_id}", headers)
    assert response.status_code == 500
    assert "error" in response.json()
