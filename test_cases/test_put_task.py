import pytest
from utils.request_utils import put_request
from data.test_data import update_task_payload, url


@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json",
        "Authorization": "Bearer <your_access_token>"
    }


def test_update_task_success(headers):
    task_id = "existing_task_id"
    response = put_request(f"{url}/{task_id}", headers, update_task_payload)
    assert response.status_code == 200
    assert response.json()["title"] == update_task_payload["title"]


def test_update_task_not_found(headers):
    task_id = "non_existent_task_id"
    response = put_request(f"{url}/{task_id}", headers, update_task_payload)
    assert response.status_code == 404
    assert "error" in response.json()


def test_update_task_internal_server_error(headers, mocker):
    task_id = "existing_task_id"
    mocker.patch("requests.put",
                 return_value=mocker.Mock(status_code=500, json=lambda: {"error": "Internal Server Error"}))
    response = put_request(f"{url}/{task_id}", headers, update_task_payload)
    assert response.status_code == 500
    assert "error" in response.json()
