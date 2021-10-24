import flask
import pickle
import json
from flask import request
import numpy as np
import pandas as pd
import sklearn.linear_model as lm
import os


app = flask.Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def condition():
    return "<h1> DOES THIS FUCKING WORK ANYMORE???!?</h1>"

@app.route("/predict", methods=['POST'])
def predict():
    # Get the information that is POSTed, silent ensures any error raises an exception and alarms go off.
    content = request.get_json()

    # The body has one key -> complaint. loads converts it to dict. Data now contains the actual complaint.
    data = content['complaint']
    
    # Take in both models which are pickled
    model1 = pickle.load(open('fitted_tfidf_to_use_MAIN.pickle', 'rb'))
    model2 = pickle.load(open("logit_finalized_MAIN.pickle", 'rb'))
    
    # First Generate Tokens and then pass that to the second model to predict situation
    tokens = model1.transform([data])
    result = model2.predict(tokens)
    
    result = {"result" : result[0]}
    return (flask.jsonify(result))

if __name__ == '__main__':
    app.run()