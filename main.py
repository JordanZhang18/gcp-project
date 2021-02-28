from flask import Flask, render_template, request
from flask import jsonify
import google.auth
from google.cloud import bigquery
#from google.cloud import bigquery_storage
from google.oauth2 import service_account
#credentials = service_account.Credentials.from_service_account_file(
#'path/to/file.json')
#project_id = 'covid19-302022'


credentials, project_id = google.auth.default(
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

bqclient = bigquery.Client(credentials= credentials,project=project_id)
#bqstorageclient = bigquery_storage.BigQueryReadClient(credentials=credentials)
    
app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("page.html", title="HOME PAGE")

@app.route("/predict")
def docs():
    return render_template("page.html", title="predict page")

@app.route("/about")
def about():
    return render_template("page.html", title="about page")
  
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)
