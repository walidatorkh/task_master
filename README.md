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

### Test scenario:

| No. | Request Type | Endpoint              | Test Description                                             | Expected Status Code | Notes                                      |
|-----|--------------|-----------------------|--------------------------------------------------------------|----------------------|--------------------------------------------|
| 1   | POST         | /tasks                | Successfully create a new task                               | 200                  | Verify the task is created with correct data |
| 2   | POST         | /tasks                | Error when creating a task with missing fields               | 400                  | Verify an error is returned for invalid data |
| 3   | POST         | /tasks                | Internal server error when creating a task                   | 500                  | Simulate server error                       |
| 4   | PUT          | /tasks/{taskId}       | Successfully update an existing task                         | 200                  | Verify the task is updated with correct data |
| 5   | PUT          | /tasks/{taskId}       | Error when updating a non-existent task                      | 404                  | Verify an error is returned for a non-existent task |
| 6   | PUT          | /tasks/{taskId}       | Internal server error when updating a task                   | 500                  | Simulate server error                       |
| 7   | GET          | /tasks/{taskId}       | Successfully retrieve details of an existing task            | 200                  | Verify the task details are correct         |
| 8   | GET          | /tasks/{taskId}       | Error when retrieving details of a non-existent task         | 404                  | Verify an error is returned for a non-existent task |
| 9   | GET          | /tasks/{taskId}       | Internal server error when retrieving task details           | 500                  | Simulate server error                       |

