from flask import Flask
app = Flask(__name__)



@app.route('/')
def index():
    return ("hello")


@app.route('/drinks')
def get_drinks():
    return {"drinks":"drink data"}