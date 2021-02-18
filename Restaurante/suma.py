from random import random
from flask import request

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "hola mundo"


@app.route('/num1')
def num1():
    return {"num1": random()}


@app.route('/num2')
def num2():
    return {"num2": random()}


@app.route('/suma', methods=['POST', 'GET'])
def suma():
    num1 = 0
    num2 = 0
    if request.method == 'POST':
        num1 = request.json['num1']
        num2 = request.json['num2']

    return {"suma": num2 + num1}


if __name__ == '__main__':
    app.run(port=1010)
