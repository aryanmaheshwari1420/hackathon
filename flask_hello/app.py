from flask import Flask,render_template,request,jsonify
import pickle
import pandas as pd
import numpy as np
# from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
app = Flask(__name__)
loaded_model = pickle.load(open('phishing.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    Url_get = request.form.get('URL')
    print(Url_get)
    
    result = loaded_model.predict([Url_get])

    # return "this result is {}".format(result)
    # print(result)
    
    if result == 'Bad':
    #     # return jsonify({'label':1})
    #     # return render_template('index.html',label=1)
        return "This is a phising website"
    else:
    #     # return jsonify({'label':-1})
    #     # return render_template('index.html',label=-1)
        return "This is not a phising website"
    # return "The Mintemp is {} , Maxtemp is{} and sunshine is{}".format(mintemp,maxtemp,sunshine)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=8001)
