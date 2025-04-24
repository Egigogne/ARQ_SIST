from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
LOG_FILE = 'log.txt'

@app.route('/log', methods=['POST'])
def log():
    entry = request.json.get('action', 'No action')
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{datetime.now()}] {entry}\n")
    return {'status': 'logged'}, 200

if __name__ == '__main__':
    app.run(port=5003)
