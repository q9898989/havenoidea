from flask import Flask
import rhino3dm as rhino

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello hello hello a'


@app.route('/abcd')
def abcd():
    return 'have no idea yet'

