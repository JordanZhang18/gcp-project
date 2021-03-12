import os
from pathlib import Path
import pandas as pd
import numpy as np
import pickle

#form_dict = {'Attendance':10000,'AVGCapcity':500,'Month':2,'Year':2001,
 #   'Performances':35,'Type':'Play','Theatre':'Cort'}

def SalePrediction(form_dict):
    df = pd.DataFrame(form_dict, index=[0])
    
    repo_path = Path(os.getcwd())
    try:
        with open( repo_path/"model.p", 'rb') as modelfile:
            lm = pickle.load(modelfile)
        with open(repo_path/"encoder.p", 'rb') as encoder:
            enc = pickle.load(encoder)    
        df[['Type','Theatre']] = enc.transform(df[['Type','Theatre']])
        pred_sale = lm.predict(df)[0]
        return "The show is expected to generate revenue of ${0}!".format(pred_sale)
    
    except:
        return 'Sorry, there was a problem processing the data entered... Please go back and double check your entries, thanks!'

#SalePrediction(form_dict)