from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    words = [
        'Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew',
        'Iceberg', 'Jicama', 'Kale', 'Lettuce', 'Mushroom', 'Napa', 'Onion', 'Pepper'
    ]
    return render_template('index.html', words=words)

@app.route('/submit', methods=['POST'])
def submit():
    placements = request.form.getlist('placement')
    elapsed_time = request.form['elapsed_time']
    print('Placements:', placements)
    print('Elapsed time:', elapsed_time)
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)
