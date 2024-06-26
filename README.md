# TaskMaster

## Instructions:

This Python functions checks API calls to the online task management service named
"TaskMaster" and handles different scenarios.
In order to be able to test the API's was created dummy server 

1. Installation

	1.1 Clone or download the Python script containing the functions (link to code ([https://github.com/walidatorkh/task_master.git](https://github.com/walidatorkh/task_master.git)).

	1.2 Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

	1.3 Install the required dependencies using pip: pip install -r requirements.txt

2. Execution

	2.1 open CMD and navigate to file location
   
	2.2 Execute pytest -v .\test_taskmaster.py

## Test Plan

### I am starting from the premise that I have read the specification document, 
I understand how the feature works, and now I will describe to you which tests I would include in the test plan

## Automation Framework Design for TaskMaster API

### 1. Test Strategy Definition:
- Define scope: Determine endpoints to be tested and types of tests: focus on testing the functionality (that include positive, negative scenarios) of creating a new task (POST
request), updating an existing task (PUT request), and retrieving task details (GET
request). 

- Test environment setup: Base URL, authentication mechanism, prerequisite data.

### 2. Framework Architecture:
- Choose testing framework: pytest.
- Organize structure: Modular components for maintainability.

### 3. Test Data Management:
- Efficient data handling: Fixtures or data factories.
- Separation: Test data from code for maintainability.

### 4. Test Case Design:
- Write test cases: Based on identified scenarios (positive/negative).
- Assertions: Validate expected API behavior (status codes, response payloads).

### 5. Integration with Version Control:
- Version control: Store scripts and resources (Git).
- Branching: Manage feature development, bug fixes.

### 6. Issues
- The specifications do not describe the URL.
- Missing specifications describe the errors code that can occur during the API calls (except: 200, 404,500)
- The server response time is not described in the specifications.
- The maximum number of requests is not described.

## TaskMaster Test Scenarios

### Test Scenario 1: Create Task

| Test Case ID | Description                                   | Endpoint     | Method | Headers                            | Payload                                                                                                                     | Expected Status | Actual Status | Pass/Fail | Notes |
|--------------|-----------------------------------------------|--------------|--------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-----------------|---------------|-----------|-------|
| TC_01        | Valid task creation                           | /tasks       | POST   | Authorization: Bearer 12345       | Valid Payload | 200             |               |           |       |
| TC_02        | Missing authorization token                   | /tasks       | POST   |                                   | Valid Payload | 500             |               |           |       |
| TC_03        | Empty title                                   | /tasks       | POST   | Authorization: Bearer 12345       | Invalid Payload | 500             |               |           |       |
| TC_04        | Title too long                                | /tasks       | POST   | Authorization: Bearer 12345       | Invalid Payload | 500             |               |           |       |
| TC_05        | Empty description                             | /tasks       | POST   | Authorization: Bearer 12345       | Invalid Payload | 500             |               |           |       |
| TC_06        | Description too long                          | /tasks       | POST   | Authorization: Bearer 12345       | Invalid Payload | 500             |               |           |       |
| TC_07        | Non-existent URL                              | /tasks/1234  | POST   | Authorization: Bearer 12345       | Valid Payload | 404             |               |           |       |
| TC_08        | Non-valid due_date format                     | /tasks       | POST   | Authorization: Bearer 12345       | Invalid Payload | 500             |               |           |       |

## Test Scenario 2: Update Task

| Test Case ID | Description                                   | Endpoint          | Method | Headers                            | Payload                                                                                                                     | Expected Status | Actual Status | Pass/Fail | Notes |
|--------------|-----------------------------------------------|-------------------|--------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-----------------|---------------|-----------|-------|
| TC_01        | Valid task update                             | /tasks/1          | PUT    | Authorization: Bearer 12345       | Valid Payload | 200             |               |           |       |
| TC_02        | Missing authorization token                   | /tasks/1          | PUT    |                                   | Valid Payload | 500             |               |           |       |
| TC_03        | Empty title                                   | /tasks/1          | PUT    | Authorization: Bearer 12345       | Invalid Payload | 500             |               |           |       |
| TC_04        | Title too long                                | /tasks/1          | PUT    | Authorization: Bearer 12345       | Invalid Payload | 500             |               |           |       |
| TC_05        | Empty description                             | /tasks/1          | PUT    | Authorization: Bearer 12345       | Invalid Payload | 500             |               |           |       |
| TC_06        | Description too long                          | /tasks/1          | PUT    | Authorization: Bearer 12345       | Invalid Payload | 500             |               |           |       |
| TC_07        | Non-existent task ID                          | /tasks/999        | PUT    | Authorization: Bearer 12345       | Valid Payload | 404             |               |           |       |
| TC_08        | Non-valid due_date format                     | /tasks/1          | PUT    | Authorization: Bearer 12345       | Invalid Payload | 500             |               |           |       |

## Test Scenario 3: Get Task

| Test Case ID | Description                                   | Endpoint          | Method | Headers                            | Expected response | Expected Status | Actual Status | Pass/Fail | Notes |
|--------------|-----------------------------------------------|-------------------|--------|-----------------------------------|---------|-----------------|---------------|-----------|-------|
| TC_01        | Valid task retrieval                          | /tasks/1          | GET    | Authorization: Bearer 12345       | {"description": "Revise and enhance test cases for API testing practices", "due_date": current_date, "id": 1, "title": "Update API Testing Practice"}| 200             |               |           |       |
| TC_02        | Missing authorization token                   | /tasks/1          | GET    |                                   |         | 500             |               |           |       |
| TC_03        | Non-existent task ID                          | /tasks/999        | GET    | Authorization: Bearer 12345       |         | 404             |               |           |       |
| TC_04        | Non-existent URL                              | /tasks/1234       | GET    | Authorization: Bearer 12345       |         | 404             |               |           |       |


