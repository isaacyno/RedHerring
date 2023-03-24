from flask import Flask, render_template, request
import pandas as pd
import random

app = Flask(__name__)

# create df
df = pd.read_csv("categories.csv")
df = df.drop("Unnamed: 0", axis=1)
df = df.reset_index(drop=True)
df_len = len(df)


@app.route('/')
def index():
    #pick 3 random categories
    allDiff = True
    
    while allDiff:
        allwords = random.sample(range(df_len), 7)
        cats = allwords[:3]
        diff = allwords[3:]
        solution = []
        #pick 4 random words per category
        count = 0
        for n in cats:
            catn = df.iloc[n]
            randomindex = random.sample(range(10), 4)
            #create solution
            solution.append(catn[randomindex].to_list())
        #pick 4 random different words from different topics as red herrings
        rh = []
        for k in diff:
            redn = df.iloc[k]
            randomindex = random.sample(range(10), 1)
            rh.append(redn[randomindex].item())
        solution.append(rh)
        truewords = [item for sublist in solution for item in sublist]
        #make sure all the words are unique
        if len(truewords) == len(set(truewords)):
            allDiff = False
    #randomize list of words
    random.shuffle(truewords)
    return render_template('index.html', words=truewords)

@app.route('/submit', methods=['POST'])
def submit():
    placements = request.form.getlist('placement')
    elapsed_time = request.form['elapsed_time']
    print('Placements:', placements)
    print('Elapsed time:', elapsed_time)
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)
