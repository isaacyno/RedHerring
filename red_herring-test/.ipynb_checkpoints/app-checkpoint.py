from flask import Flask, render_template, request
import pandas as pd
import random

app = Flask(__name__)

# create df
df = pd.read_csv("categories.csv")
df_len = len(df)


@app.route('/')
def index():
    # get 7 random rows from the df, the first 3 will be for the 3 categories, the last 4 for red herrings
    my_rows = random.sample(range(df_len), 7)
    L = []
    # add the category lists
    for i in my_rows[:3]:
        L.append(list(df.iloc[i, random.sample(range(10), 4)]))
    # red herring list
    rh = []
    for j in my_rows[3:]:
        rh.append(df.iloc[j, random.sample(range(10), 1)].item())
    L.append(rh)
    return render_template('index.html', words=L)

@app.route('/submit', methods=['POST'])
def submit():
    placements = request.form.getlist('placement')
    elapsed_time = request.form['elapsed_time']
    print('Placements:', placements)
    print('Elapsed time:', elapsed_time)
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)
