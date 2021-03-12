import os
from pathlib import Path
import pandas as pd
import numpy as np
import pickle

def SalePrediction(form_dict):

    repo_path = Path(os.getcwd())
    lm = pickle.load(repo_path / "model.p")
    enc= pickle.load(repo_path / "encoder.p")
    try:
        df = pd.DataFrame(form_dict, index=[0])
        pred_sale = lm.predict(enc.transform(df))[0]


        return "The show is expected to generate revenue of ${1}!".format(pred_sale)

    except:
        return 'Sorry, there was a problem processing the data entered... Please go back and double check your entries, thanks!'