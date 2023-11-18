import uuid
import time
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)
unique_id = str(uuid.uuid4())
status = {"timestamp": "", "unique_id": ""}

def log_output():
    global status
    while True:
        status["timestamp"] = datetime.utcnow().isoformat() + 'Z'
        status["unique_id"] = unique_id
        print(f"{status['timestamp']}: {status['unique_id']}")
        time.sleep(5)

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(status)

if __name__ == '__main__':
    # Start the logging loop in a separate thread
    import threading
    log_thread = threading.Thread(target=log_output)
    log_thread.daemon = True
    log_thread.start()

    # Run the Flask app
    app.run(host='0.0.0.0', port=3000)
