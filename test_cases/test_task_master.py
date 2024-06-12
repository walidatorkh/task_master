import os
import subprocess
import sys
import time

from data.test_data import url, headers, headers1, post_payload, put_payload
import pytest
import requests
import json


@pytest.fixture(scope="module", autouse=True)
def start_flask_app():
    # Use the Python executable from the virtual environment
    python_executable = os.path.join(sys.prefix, 'Scripts', 'python.exe')

    # Start the Flask server
    server = subprocess.Popen(
        [python_executable, "C:\\Automation\\task_master\\dummy_server\\pyserver.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Wait for the server to start
    time.sleep(15)  # Increase sleep time to ensure server starts

    # Check if server started successfully
    return_code = server.poll()
    if return_code is not None:
        stdout, stderr = server.communicate()
        print("Server failed to start. Output:")
        print(stdout.decode())
        print(stderr.decode())
        raise RuntimeError("Server failed to start")

    yield

    # Terminate the server after tests
    server.terminate()
    server.wait()


@pytest.mark.parametrize("endpoint, headers, payload, expected_status", [
    ("/tasks", headers, post_payload, 200),  # Successful creation
    ("/@tasks", headers, post_payload, 404),  # Non-existent endpoint
    ("/tasks", headers1, post_payload, 500),  # Server error
])
def test_create_task(endpoint, headers, payload, expected_status):
    response = requests.post(f"{url}{endpoint}", headers=headers, json=payload)
    assert response.status_code == expected_status


@pytest.mark.parametrize("task_id, headers, payload, expected_status", [
    (1, headers, put_payload, 200),  # Successful update
    (222, headers, put_payload, 404),  # Non-existent id
    (1, headers1, put_payload, 500),  # Server error
])
def test_update_task(task_id, headers, payload, expected_status):
    response = requests.put(f"{url}/tasks/{task_id}", headers=headers, json=payload)
    assert response.status_code == expected_status


@pytest.mark.parametrize("task_id, headers, expected_status", [
    (1, headers, 200),  # Valid task
    (22, headers, 404),  # Non-existent task
    (1, headers1, 500),  # Server error
])
def test_get_task(task_id, headers, expected_status):
    response = requests.get(f"{url}/tasks/{task_id}", headers=headers)
    assert response.status_code == expected_status
