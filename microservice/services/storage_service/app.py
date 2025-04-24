from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
FILE = 'tasks.json'

def read_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, 'r') as f:
        try:
            return json.load(f)
        except:
            return []

def write_tasks(tasks):
    with open(FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(read_tasks())

@app.route('/tasks', methods=['POST'])
def add_task():
    tasks = read_tasks()
    new_task = request.json
    new_task['id'] = len(tasks) + 1
    new_task['completed'] = False
    tasks.append(new_task)
    write_tasks(tasks)
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    tasks = read_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            break
    write_tasks(tasks)
    return jsonify({"status": "completed"}), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = read_tasks()
    tasks = [t for t in tasks if t['id'] != task_id]
    write_tasks(tasks)
    return jsonify({"status": "deleted"}), 200

if __name__ == '__main__':
    app.run(port=5002)
