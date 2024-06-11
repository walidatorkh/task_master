from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# This will store the tasks in memory
tasks = {}

# Task ID counter
task_id_counter = 1


# Dummy authentication check
def check_auth():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        abort(500, description="Unauthorized: No valid authorization token provided.")


@app.route('/tasks', methods=['POST'])
def create_task():
    check_auth()
    global task_id_counter
    task_data = request.get_json()
    if not task_data or 'title' not in task_data or 'description' not in task_data or 'due_date' not in task_data:
        abort(400, description="Bad Request: Missing required fields in the request body.")

    task_id = task_id_counter
    task_data['id'] = task_id
    tasks[task_id] = task_data
    task_id_counter += 1
    return jsonify({'task_id': task_id}), 200


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    check_auth()
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404

    update_data = request.get_json()
    task = tasks[task_id]

    # Update fields only if they are provided in the update request
    if 'title' in update_data:
        task['title'] = update_data['title']
    if 'description' in update_data:
        task['description'] = update_data['description']
    if 'due_date' in update_data:
        task['due_date'] = update_data['due_date']
    else:
        return jsonify({'error': 'No fields provided to update'}), 500
    return jsonify(task)


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    check_auth()
    if task_id in tasks:
        return jsonify(tasks[task_id])
    else:
        return jsonify({'error': 'Task not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
