from flask import Flask, render_template, request
import random
import pandas as pd
import numpy as np

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test/')
def test():
    return render_template('test.html')

@app.route('/test2/')
def test2():
    return render_template('test2.html')

@app.route('/dropped', methods=['POST'])
def dropped():
    x = request.form['x']
    y = request.form['y']
    print(f'Element dropped at position: ({x}, {y})')
    return 'OK'