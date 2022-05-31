from datetime import datetime
from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Received api call at: " + datetime.now())
    time.sleep(100000)
    return "<p>Hello, World!</p>"