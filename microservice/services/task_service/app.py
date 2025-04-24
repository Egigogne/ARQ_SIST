from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

STORAGE_URL = 'http://localhost:5002'
LOGGING_URL = 'http://localhost:5003'

@app.route('/tasks', methods=['GET'])
def get_tasks():
    res = requests.get(f"{STORAGE_URL}/tasks")
    return jsonify(res.json())

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json
    res = requests.post(f"{STORAGE_URL}/tasks", json=task)
    requests.post(f"{LOGGING_URL}/log", json={"action": f"Tarea agregada: {task['title']}"})
    return res.content, res.status_code

@app.route('/tasks/<int:task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    res = requests.put(f"{STORAGE_URL}/tasks/{task_id}/complete")
    requests.post(f"{LOGGING_URL}/log", json={"action": f"Tarea completada: {task_id}"})
    return res.content, res.status_code

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    res = requests.delete(f"{STORAGE_URL}/tasks/{task_id}")
    requests.post(f"{LOGGING_URL}/log", json={"action": f"Tarea eliminada: {task_id}"})
    return res.content, res.status_code

if __name__ == '__main__':
    app.run(port=5001)
