#import relevant libraries for flask,html rendering and loading the ML model
from flask import Flask,request,url_for,redirect,render_template
import pickle
import pandas as pd
import joblib
app = Flask(__name__)
#model = pickle.load(open("model.pkl","rb"))
model = joblib.load("model.pkl")
#scale = pickle.load(open("scale.pkl","rb"))
scale = joblib.load("scale.pkl")
@app.route("/")
def landingPage():
    return render_template('index.html')
@app.route("/predict",methods=['POST','GET'])
def predict():

    Pregnancies = request.form['1']
    Glucose = request.form['2']
    BloodPressure = request.form['3']
    SkinThickness = request.form['4']
    Insulin = request.form['5']
    BMI = request.form['6']
    DiabetesPedigreeFunction = request.form['7']
    Age = request.form['8']

    rowDF=pd.DataFrame([pd.Series([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,
           Age])])
    rowDF_new=pd.DataFrame(scale.transform(rowDF))
    print(rowDF_new)
        #  model prediction 
    prediction= model.predict_proba(rowDF_new)
    print(f"The  Predicted values is :{prediction[0][1]}")
    
    if prediction[0][1] >= 0.5:
        valPred = round(prediction[0][1],3)
        print(f"The Round val {valPred*100}%")
        return render_template('result.html',pred=f'You have a chance of having diabetes.\n\nProbability of you being a diabetic is {valPred*100}%.\n\nAdvice : Exercise Regularly')
    else:
        valPred = round(prediction[0][0],3)

        return render_template('result.html',pred=f'Congratulations!!!, You are in a Safe Zone.\n\n Probability of you being a non-diabetic is {valPred*100}%.\n\n Advice : Exercise Regularly and maintain like this..!')


if __name__ == '__main__':
    app.run(debug=True)