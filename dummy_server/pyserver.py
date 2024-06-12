from flask import Flask, jsonify, request, abort
from datetime import datetime

app = Flask(__name__)

# This will store the tasks in memory
tasks = {}

# Task ID counter
task_id_counter = 1


# Validation function for headers
def validate_headers():
    content_type = request.headers.get('Content-Type')
    if content_type != 'application/json':
        abort(500, description="Bad Request: 'Content-Type' must be 'application/json'.")


# Dummy authentication check
def check_auth():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        abort(500, description="Unauthorized: No valid authorization token provided.")


# Validation function for task data
def validate_task_data(task_data):
    if not task_data:
        abort(500, description="Bad Request: Missing request body.")
    if 'title' not in task_data or not task_data['title']:
        abort(500, description="Bad Request: 'title' is required and cannot be empty.")
    if len(task_data['title']) > 256:
        abort(500, description="Bad Request: 'title' cannot be more than 256 characters.")
    if 'description' not in task_data or not task_data['description']:
        abort(500, description="Bad Request: 'description' is required and cannot be empty.")
    if len(task_data['description']) > 1024:
        abort(500, description="Bad Request: 'description' cannot be more than 1024 characters.")
    current_date = datetime.now().strftime("%Y-%m-%d")
    if 'due_date' not in task_data:
        task_data['due_date'] = current_date
    elif task_data['due_date'] != current_date:
        abort(500, description=f"Bad Request: 'due_date' must be {current_date}.")
    try:
        datetime.fromisoformat(task_data['due_date'])
    except ValueError:
        abort(500, description="Bad Request: 'due_date' must be a valid ISO format date.")


@app.route('/tasks', methods=['POST'])
def create_task():
    check_auth()
    validate_headers()
    global task_id_counter
    task_data = request.get_json()
    validate_task_data(task_data)

    task_id = task_id_counter
    task_data['id'] = task_id
    tasks[task_id] = task_data
    task_id_counter += 1
    return jsonify({'task_id': task_id}), 200


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    check_auth()
    validate_headers()
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404

    update_data = request.get_json()
    validate_task_data(update_data)

    task = tasks[task_id]
    task['title'] = update_data['title']
    task['description'] = update_data['description']
    task['due_date'] = update_data['due_date']
    return jsonify(task)


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    check_auth()
    validate_headers()
    if task_id in tasks:
        return jsonify(tasks[task_id])
    else:
        return jsonify({'error': 'Task not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
