import uuid
import time
from datetime import datetime
from flask import Flask

app = Flask(__name__)
unique_id = str(uuid.uuid4())

def log_output():
    while True:
        timestamp = datetime.utcnow().isoformat() + 'Z'
        print(f"{timestamp}: {unique_id}")
        time.sleep(5)

if __name__ == '__main__':
    log_output()
