import os
import subprocess
import sys
import time
import pytest
import requests
from ..data import test_data as data


url = 'http://localhost:5000'


@pytest.fixture(scope="module", autouse=True)
def start_dummy_server():
    python_executable = os.path.join(sys.prefix, 'Scripts', 'python.exe')

    server = subprocess.Popen(
        [python_executable, "C:\\Automation\\task_master\\dummy_server\\pyserver.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

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


@pytest.mark.parametrize("test_input", [
    ("TC_01_POST", "Valid task creation", "/tasks", "POST", data.headers, data.post_payload_valid, 200),
    ("TC_02_POST", "Missing authorization token", "/tasks", "POST", data.no_auth, data.post_payload_valid, 500),
    ("TC_03_POST", "Empty title", "/tasks", "POST", data.headers, data.post_payload_empty_title, 500),
    ("TC_04_POST", "Title too long", "/tasks", "POST", data.headers, data.post_payload_invalid_title_long, 500),
    ("TC_05_POST", "Empty description", "/tasks", "POST", data.headers, data.post_payload_invalid_description_empty, 500),
    ("TC_06_POST", "Description too long", "/tasks", "POST", data.headers, data.post_payload_long_description, 500),
    ("TC_07_POST", "Non-existent URL", "/tasks@", "POST", data.headers, data.post_payload_valid, 404),
    ("TC_08_POST", "Non-valid due_date format", "/tasks", "POST", data.headers, data.post_payload_invalid_due_date, 500),
    ("TC_09_POST", "Missing value in headers", "/tasks", "POST", data.headers_invalid, data.post_payload_invalid_due_date,
     500)
])
def test_create_task(test_input):
    tc_id, description, endpoint, method, headers, payload, expected_status = test_input
    # Measure the start time
    start_time = time.time()
    # Make the request
    response = requests.request(method, f"{url}{endpoint}", headers=headers, json=payload)
    # Measure the end time
    end_time = time.time()
    # Calculate the duration
    response_time = end_time - start_time
    # Assert the response time is within acceptable limits (e.g., 2 seconds)
    assert response_time <= 5, f"Response time exceeded: {response_time} seconds"
    assert response.status_code == expected_status


@pytest.mark.parametrize("test_input", [
    ("TC_01_PUT", "Valid task update", "/tasks", '/1', "PUT", data.headers, data.put_payload_valid, 200),
    ("TC_02_PUT", "Missing authorization token", "/tasks", '/1', "PUT", data.no_auth, data.put_payload_valid, 500),
    ("TC_03_PUT", "Empty title", "/tasks", '/1', "PUT", data.headers, data.put_payload_empty_title, 500),
    ("TC_04_PUT", "Title too long", "/tasks", '/1', "PUT", data.headers, data.put_payload_long_title, 500),
    ("TC_05_PUT", "Empty description", "/tasks",  '/1', "PUT", data.headers, data.put_payload_empty_description, 500),
    ("TC_06_PUT", "Description too long", "/tasks", '/1', "PUT", data.headers, data.put_payload_long_description, 500),
    ("TC_07_PUT", "Non-existent task ID", "/tasks", '/111', "PUT", data.headers, data.put_payload_valid, 404),
    ("TC_08_PUT", "Non-valid due_date format", "/tasks", '/1', "PUT", data.headers, data.put_payload_invalid_due_date, 500),
    ("TC_09_PUT", "Missing value in headers", "/tasks", '/1', "PUT", data.headers_invalid, data.put_payload_valid, 500)
])
def test_update_task(test_input):
    test_id, description, endpoint, task_id, method, headers, payload, expected_status = test_input
    start_time = time.time()
    response = requests.put(f"{url}{endpoint}{task_id}", headers=headers, json=payload)
    end_time = time.time()
    response_time = end_time - start_time
    assert response_time <= 5, f"Response time exceeded: {response_time} seconds"
    assert response.status_code == expected_status


@pytest.mark.parametrize("test_input", [
    ("TC_01_GET", "Valid task retrieval", "/tasks", '/1', "GET", data.headers, None, 200),
    ("TC_02_GET", "Missing authorization token", "/tasks", '/1', "GET", data.no_auth, None, 500),
    ("TC_03_GET", "Non-existent task ID", "/tasks", '/999', "GET", data.headers, None, 404),
    ("TC_04_GET", "Non-existent URL", "/tasks@", '/1', "GET", data.headers, None, 404),
    ("TC_05_GET", "Missing value in headers", "/tasks", '/1', "GET", data.headers_invalid, None, 500),
])
def test_get_task(test_input):
    test_id, description, endpoint, task_id, method, headers, payload, expected_status = test_input
    start_time = time.time()
    response = requests.get(f"{url}{endpoint}{task_id}", headers=headers)
    end_time = time.time()
    response_time = end_time - start_time
    assert response_time <= 5, f"Response time exceeded: {response_time} seconds"
    assert response.status_code == expected_status
