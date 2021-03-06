from flask import Flask, render_template, request, url_for
import os
import pickle
import model as m
# from flaskalchemy.flaskalchemy import FlaskAlchemy
app=Flask(__name__,template_folder='templates')
#model = pickle.load(open('expense.pkl','rb'))
@app.route("/" , methods = ['GET', 'POST'])# , methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        # if request.form['Prediction']:
        return render_template('survey.html')
    return render_template("index.html")

@app.route("/survey.html")
def formpage():
    return render_template("survey.html")

@app.route("/survey" , methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        name = request.form['name']
        q2 = request.form['q2']
        q3 = request.form['q3']
        q4 = request.form['q4']
        q5 = request.form['q5']
        q6 = request.form['q6']
        q7 = request.form['q7']
        
        q2 = int(q2)
        q3 = int(q3)
        q4 = int(q4)
        q5 = int(q5)
        q6 = int(q6)
        q7 = int(q7)
        print(q2, q3, q4, q5, q6 ,q7)
        prediction = m.model(q2,q3,q4,q5,q6,q7)
        
        # print(type(prediction))
        if prediction > 10:
            return render_template("negative.html" , prediction = float(prediction))
        
            
    return render_template("survey.html")




if __name__ == "__main__":
    app.run(debug=True)