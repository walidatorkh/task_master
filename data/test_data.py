from datetime import datetime


# Define the API endpoint
url = "http://localhost:5000"

# Define time format
current_date = datetime.now().strftime("%Y-%m-%d")

# Define payloads

post_payload_valid = {
    "title": "Complete API Testing Practice",
    "description": "Write test cases and execute them for API testing practices",
    "due_date": current_date
}

post_payload_invalid_title_long = {
    "title": "A" * 257,  # Too long title
    "description": "Write test cases and execute them for API testing practices",
    "due_date": current_date
}

post_payload_empty_title = {
    "title": "",
    "description": "This payload has an empty title",
    "due_date": current_date
}

post_payload_invalid_description_empty = {
    "title": "Complete API Testing Practice",
    "description": "",  # Empty description
    "due_date": current_date
}


post_payload_long_description = {
    "title": "API Testing",
    "description": "A" * 1025,
    "due_date": current_date
}

post_payload_invalid_due_date = {
    "title": "Complete API Testing Practice",
    "description": "Write test cases and execute them for API testing practices",
    "due_date": "20-06-2024" # Invalid date format
}

put_payload_valid = {
    "title": "Update API Testing Practice",
    "description": "Revise and enhance test cases for API testing practices",
    "due_date": current_date
}

put_payload_empty_title = {
    "title": "",
    "description": "Write test cases and execute them for API testing practices",
    "due_date": current_date
}

put_payload_long_title = {
    "title": "A" * 257,
    "description": "This payload has a title that is too long",
    "due_date": current_date
}

put_payload_long_description = {
    "title": "Update API Testing Practice",
    "description": "A" * 1025,  # Too long description
    "due_date": current_date
}

put_payload_empty_description = {
    "title": "Update API Testing Practice",
    "description": "",
    "due_date": current_date
}

put_payload_invalid_due_date = {
    "title": "Update API Testing Practice",
    "description": "Revise and enhance test cases for API testing practices",
    "due_date": "invalid-date"  # Invalid date format
}

expected_response = {
            "description": "Revise and enhance test cases for API testing practices",
            "due_date": current_date,
            "id": 1,
            "title": "Update API Testing Practice"
        }

valid_schema = {
        "id": {"type": "number"},
        "title": {"type": "string"},
        "description": {"type": "string"},
        "due_date": {"type": "string"}
    }

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 12345"
}


headers_invalid = {
    "Content-Type": "",
    "Authorization": "Bearer 12345"
}
no_auth = {
    "Content-Type": "application/json",
    "Authorization": "invalid_token"
}
