from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle

# loading model
df = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


def recommendation(Title_df):
    idx = df[df['Title'] == Title_df].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])

    Titles = []
    for m_id in distances[1:21]:
        Titles.append(df.iloc[m_id[0]].Title)

    return Titles



app = Flask(__name__)

@app.route('/')
def index():
    names = list(df['Title'].values)
    return render_template('index.html',name = names)
@app.route('/recom',methods=['POST'])
def mysong():
    user_Title = request.form['names']
    Titles = recommendation(user_Title)

    return render_template('index.html',Titles=Titles)


# python
if __name__ == "__main__":
    app.run(debug=True)