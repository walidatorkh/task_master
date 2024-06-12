# task_master
About testing the API of an online task management service named "TaskMaster". 
## Test Plan

### I am starting from the premise that I have read the specification document, 
I understand how the feature works, and now I will describe to you which tests I would include in the test plan

## Automation Framework Design for TaskMaster API

### 1. Test Strategy Definition:
- Define scope: Determine endpoints to be tested and types of tests.
- Test environment setup: Base URL, authentication mechanism, prerequisite data.

### 2. Framework Architecture:
- Choose testing framework: pytest, unittest, or custom framework. (choosen pytest)
- Organize structure: Modular components for maintainability.
- Reusable utilities: Helper functions for HTTP requests, response parsing, authentication.

### 3. Test Data Management:
- Efficient data handling: Fixtures or data factories.
- Separation: Test data from code for maintainability.
- Mock data: For scenarios not requiring actual API calls.

### 4. Test Case Design:
- Write test cases: Based on identified scenarios (positive/negative).
- Grouping: Organize into suites/modules.
- Assertions: Validate expected API behavior (status codes, response payloads).

### 5. Execution and Reporting:
- Run tests: Using chosen framework.
- Reporting: Detailed test reports (pass/fail status, execution time).
- CI Integration: Automated execution on code changes or schedules.

### 6. Error Handling and Debugging:
- Exception handling: Gracefully handle errors during execution.
- Logging: Capture request/response details, stack traces.

### 7. Integration with Version Control:
- Version control: Store scripts and resources (Git).
- Branching: Manage feature development, bug fixes.

### 8. Maintenance and Updates:
- Regular review: Update test cases to reflect API changes.
- Documentation: Framework guidelines, setup instructions.
- Feedback incorporation: Improve test coverage and efficiency.

## Test Scenarios

### Test Scenario 1: Create Task

| Test Case ID | Description                 | Endpoint  | Headers          | Payload          | Expected Status | Actual Status | Pass/Fail | Notes |
|--------------|-----------------------------|-----------|------------------|------------------|-----------------|---------------|-----------|-------|
| TC1          | Successful creation         | `/tasks`  | Valid headers    | Valid payload    | 200             |               |           |       |
| TC2          | Non-existent endpoint       | `/@tasks` | Valid headers    | Valid payload    | 404             |               |           |       |
| TC3          | Server error due to headers | `/tasks`  | Invalid headers  | Valid payload    | 500             |               |           |       |

**Steps:**
1. Use the appropriate HTTP method (POST) for creating tasks.
2. Send requests to the specified endpoints with given headers and payloads.
3. Verify the response status code matches the expected status.

### Test Scenario 2: Update Task

| Test Case ID | Description                 | Endpoint       | Headers          | Payload          | Expected Status | Actual Status | Pass/Fail | Notes |
|--------------|-----------------------------|----------------|------------------|------------------|-----------------|---------------|-----------|-------|
| TC4          | Successful update           | `/tasks/1`     | Valid headers    | Valid payload    | 200             |               |           |       |
| TC5          | Non-existent task ID        | `/tasks/222`   | Valid headers    | Valid payload    | 404             |               |           |       |
| TC6          | Server error due to headers | `/tasks/1`     | Invalid headers  | Valid payload    | 500             |               |           |       |

**Steps:**
1. Use the appropriate HTTP method (PUT) for updating tasks.
2. Send requests to the specified endpoints with given headers and payloads.
3. Verify the response status code matches the expected status.


### Test Scenario 3: Get Task (GET)


## Test Scenario 3: Get Task

| Test Case ID | Description                 | Endpoint       | Headers          | Expected Status | Actual Status | Pass/Fail | Notes |
|--------------|-----------------------------|----------------|------------------|-----------------|---------------|-----------|-------|
| TC7          | Valid task                  | `/tasks/1`     | Valid headers    | 200             |               |           |       |
| TC8          | Non-existent task ID        | `/tasks/22`    | Valid headers    | 404             |               |           |       |
| TC9          | Server error due to headers | `/tasks/1`     | Invalid headers  | 500             |               |           |       |

**Steps:**
1. Use the appropriate HTTP method (GET) for retrieving tasks.
2. Send requests to the specified endpoints with given headers.
3. Verify the response status code matches the expected status.


