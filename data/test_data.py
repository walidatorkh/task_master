# Test data for creating a new task
from datetime import datetime

# Define the API endpoint
url = "http://localhost:5000"

# Define the headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 12345"
}
headers1 = {
    "Content-Type": "application/json",
    "Authorization": "12345"
}
current_date = datetime.now().strftime("%Y-%m-%d")
# Define the payloads
post_payload = {
    "title": "Complete API Testing Practice",
    "description": "Write test cases and execute them for API testing practices",
    "due_date": current_date
}

put_payload = {
    "title": "Update API Testing Practice",
    "description": "Revise and enhance test cases for API testing practices",
    "due_date": current_date
}

# Placeholder for error 500 scenario (no specific data needed)
error_500 = {}
