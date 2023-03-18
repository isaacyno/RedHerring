from flask import Flask, render_template, request
import random
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.oute('/')
def index():
    return render_template('test.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
