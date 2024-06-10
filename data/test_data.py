# Test data for creating a new task
from datetime import datetime


# Define the API endpoint
url = "https://taskmaster.com/api/tasks"


current_date = datetime.now().strftime("%Y-%m-%d")
create_task_payload = {
    "title": "Complete API Testing Practice",
    "description": "Write test cases and execute them for API testing practices",
    "due_date": current_date
}

# Test data for creating a task with missing fields
create_task_missing_fields = {
    "description": "Write test cases and execute them for API testing practices",
    "due_date": current_date
}

# Test data for updating an existing task
update_task_payload = {
    "title": "Update API Testing Practice",
    "description": "Revise and enhance test cases for API testing practices",
    "due_date": current_date
}

# Placeholder for error 500 scenario (no specific data needed)
error_500 = {}