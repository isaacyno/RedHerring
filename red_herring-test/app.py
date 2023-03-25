from flask import Flask, render_template, request
import pandas as pd
import random

app = Flask(__name__)

# create df
df = pd.read_csv("categories.csv")
df = df.drop("Unnamed: 0", axis=1)
df = df.reset_index(drop=True)
df_len = len(df)
#solution is accessed both in index and submit pages
solution = []

@app.route('/')
def index():
    #pick 3 random categories
    allDiff = True
    #continue to make sure all the words are unique
    while allDiff:
        #sample 7 of the categories
        allwords = random.sample(range(df_len), 7)
        #first three categories are the true categories
        cats = allwords[:3]
        #final four categories will comprise of the red-herring words
        diff = allwords[3:]
        global solution
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
    #get the words from the draggable boxes
    placements = request.form['placement']
    #get the time it took
    elapsed_time = request.form['elapsed_time']
    #eliminate a floating comma
    placements = placements[1:]
    #create a list of words separated by commas
    wordList = placements.split(",")
    #split the solution into cateogires for checking
    cat1 = wordList[0:4]
    cat2 = wordList[4:8]
    cat3 = wordList[8:12]
    cat4 = wordList[12:16]
    #check to see if the three categories are correct
    status = [False, False, False]
    #check for all permutations of words inside a category and permutations of categories with the solution key
    if set(solution[0])==set(cat1):
        status[0] = True
    if set(solution[0])==set(cat2):
        status[0] = True
    if set(solution[0])==set(cat3):
        status[0] = True
    if set(solution[1])==set(cat1):
        status[1] = True
    if set(solution[1])==set(cat2):
        status[1] = True
    if set(solution[1])==set(cat3):
        status[1] = True
    if set(solution[2])==set(cat1):
        status[2] = True
    if set(solution[2])==set(cat2):
        status[2] = True
    if set(solution[2])==set(cat3):
        status[2] = True
    #check to see if the solution is correct
    for check in status:
        #if solution is incorrect, print an incorrect message and show solutions
        if check == False:
            message = "Incorrect. The solutions is the following. <br />"
            i = 1
            for cats in solution:
                if i != 4:
                    message = message + "Category " + str(i) + ": "
                else:
                    message = message + "Red-herrings: "
                for words in cats:
                    message = message + words + " "
                message = message + '<br />'
                i += 1
            return message
    #if the solution is correct, state the time it took to complete the game
    return "Congratulations! You completed the game in " + elapsed_time 


if __name__ == '__main__':
    app.run(debug=True)
