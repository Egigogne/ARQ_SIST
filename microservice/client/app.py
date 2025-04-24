from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

TASK_SERVICE_URL = "http://localhost:5001"

@app.route('/')
def index():
    res = requests.get(f"{TASK_SERVICE_URL}/tasks")
    tasks = res.json()
    return render_template("index.html", tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    if title:
        requests.post(f"{TASK_SERVICE_URL}/tasks", json={"title": title})
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    requests.put(f"{TASK_SERVICE_URL}/tasks/{task_id}/complete")
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    requests.delete(f"{TASK_SERVICE_URL}/tasks/{task_id}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5000)
