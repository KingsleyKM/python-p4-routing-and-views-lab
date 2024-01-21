#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views'

@app.route('/print/<parameter>')
def print_string(parameter):
    return f'The parameter value is :{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers ='\n'.join(str(num) for num in range(parameter + 10))
    return numbers

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = float(num1) + float(num2)
    elif operation == '-':
        result = float(num1) - float(num2)
    elif operation == '*':
        result = float(num1) * float(num2)
    elif operation == 'div':
        if num2 != 0:
            result = float(num1) / float(num2)
    elif operation == '%':
        result = float(num1) % float(num2)
    
    if result is not None:
        return f'The result is: {result}'
    else:
        return 'Invalid operation or division by zero.'
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
