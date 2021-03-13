import os
from pathlib import Path
import pandas as pd
import numpy as np
import pickle
from google.cloud import storage


#form_dict = {'Attendance':10000,'AVGCapcity':500,'Month':2,'Year':2001,
    #'Performances':35,'Type':'Play','Theatre':'Cort'}
CLOUD_STORAGE_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']
# Create a Cloud Storage client.

#os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\jorda\AppData\Roaming\gcloud\application_default_credentials.json"

gcs = storage.Client()

 #Get the bucket that the file will be uploaded to.
bucket = gcs.get_bucket('zhang-msds433.appspot.com')

 #Create a new blob and upload the file's content.
modelfile = bucket.blob('model.p')
encoderfile=bucket.blob('encoder.p')
mymodel=modelfile.download_as_string()
myenconder=encoderfile.download_as_string()
def SalePrediction(form_dict):
    df = pd.DataFrame(form_dict, index=[0])
    
    
    try:
        lm = pickle.loads(mymodel)
        enc = pickle.loads(myenconder)    
        df[['Type','Theatre']] = enc.transform(df[['Type','Theatre']])
        pred_sale = lm.predict(df)[0]
        return "The show is expected to generate revenue of ${0}!".format(pred_sale)
    
    except:
        return 'Sorry, there was a problem processing the data entered... Please go back and double check your entries, thanks!'

#SalePrediction(form_dict)