from flask import Flask, request, render_template, redirect, url_for
from mymodel import SalePrediction
import pandas as pd
import os
from pathlib import Path


app = Flask(__name__)


@app.route('/')
def Hub():
    return render_template('hub.html')


@app.route('/Predictor')
def SalePredictor():
    return render_template('Predictor.html')



@app.route('/Predictor', methods=['POST'])
def SalePredictorPost():
    
    form_dict = {'Attendance':request.form['Attendance'],'AVGCapcity':request.form['AVGCapcity'],'Month':request.form['Month'],'Year':request.form['Year'],
    'Performances':request.form['Performances'],'Type':request.form['Type'],'Theatre':request.form['Theatre']}
    final_output = SalePrediction(form_dict)
    
    return render_template('PredictorPost.html', final_output=final_output)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=False)


