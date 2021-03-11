import json
import logging
import os

import pickle
from flask import Flask, request
from google.cloud import storage

MODEL_BUCKET = os.environ['zhang-msds433.appspot.com']
MODEL_FILENAME = os.environ['zhang-msds433.appspot.com/model']
MODEL = None

app = Flask(__name__)


@app.before_first_request
def _load_model():
    # Get the model information 
    global MODEL
    client = storage.Client()
    bucket = client.get_bucket(MODEL_BUCKET)
    blob = bucket.get_blob(MODEL_FILENAME)
    s = blob.download_as_string()
    MODEL = pickle.loads(s)


@app.route('/predict', methods=['POST'])
def predict():
    X = request.get_json()
    y = MODEL.predict(X).tolist()
    return json.dumps({'predicted_Gross': y})


@app.errorhandler(500)
def server_error(e):
    # log error
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
