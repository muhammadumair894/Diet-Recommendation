from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
import sklearn
from sklearn.linear_model import LogisticRegression
#from sklearn.externals import joblib as ld
from flask_ngrok import run_with_ngrok
from flask import Flask,jsonify
import joblib
import re

#loading trained model
model =joblib.load(r'Model\trainedModel.pkl')
model2 =joblib.load(r'Model\trainedModel2.pkl')
model3 =joblib.load(r'Model\trainedModel3.pkl')
#Loading decoders
Decode_Dis =joblib.load(r'Model\lebelEncode_Dis.pkl')
Decode_BF =joblib.load(r'Model\lebelEncode_breakfast.pkl')
Decode_Lu =joblib.load(r'Model\lebelEncode_lunch.pkl')
Decode_Din =joblib.load(r'Model\lebelEncode_dinner.pkl')
print(sklearn.__version__)

#sample

#Flask App

app = Flask(__name__)
run_with_ngrok(app)  # starts ngrok when the app is running

#"
#
@app.route("/<int:Age>/<int:Weight>/<int:Height>/<int:Disease>")
def home(Age, Weight, Height, Disease):
    p = []
    p += [Age, Weight, Height, Disease]

    arr = np.array([p])
    predict_Breakfast = Decode_BF.inverse_transform(model.predict(arr))
    predict_Lunch =Decode_Lu.inverse_transform(model2.predict(arr))
    predict_Dinner =Decode_Din.inverse_transform(model3.predict(arr))
    result = "BreakFast: " +str(predict_Breakfast)+ " Lunch: "+str(predict_Lunch)+" Dinner: "+str(predict_Dinner)
    result = re.sub('\ |\?|\.|\!|\/|\;|', ' ', result)

    return jsonify(result)


app.run()
