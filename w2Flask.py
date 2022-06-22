from flask import Flask
import rhino3dm

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello hello hello a'