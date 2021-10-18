## Broadway Show's Revenue Predictor

**Background**

The COVID-19 pandemic has put a halt to many sectors of the economy, and the live performance industry is particularly affected by it. The Broadway Theatres has closed abruptly in March 2020 and will not be able to open until at least May 2021. The shutdown has incurred devastating financial state to the live performances and thus an accurate and effective budgeting practice is critical for the recovery of the performance industry, particularly plays and musicals on Broadway, which usually has high budget and high risk. To fulfill this need, a web-based application is developed to predict the gross revenue of a particular show, with the expected attendance, theatre capacity, time, and type of performance, as well as the name of Theatre as input. This application will help producers to evaluate potential box office income and to make more realistic budgets. An improved change of profitability will benefit the recovery of show business as a whole in the long run.

**Data Processing and Modeling**

The training dataset is acquired from the CORGIS Dataset Project. This library holds data about over Broadway shows, grouped over weeklong periods. Only shows that reported capacity were included, so the dataset stretches back to the 1990s. The dataset is made available by the Broadway League (the national trade association for the Broadway industry), and it contains around 32,000 rows.

Google cloud functions are used for downloading the csv file to Google Cloud Storage, as well as reading and loading into Google BigQuery. The schema of dataset includes 12 keys, and each row corresponds to a weekly performance and revenue record of a particular show. BigQuery is used to aggregate the data by each show, and the theatre it was performed in. Some critical elements of the aggregated data are (These attributes were used to train the model and as input for predictions):

Attendance: The total number of people who attended performances over the whole length.

AVG Capacity: The average percentage of the theatre that was filled during the whole performance period.

Month and Year of a performance: If a performance ranges across multiple month or year, the average value is calculated as input.

Performances: The total number of performances; Type: Either "Musical" or "Play".

The label (object of prediction) is total gross revenue, measured in USD.

BigQuery ML is used to train the models. Both multi-regression model and random-forest models are trained and evaluated, with 10% of data set as validation. The random-forest model yields better accuracy, possibly due to a stronger ability to adept to categorical values. The trained model has a Mean Absolute Error (MAE) of $1.6 Million, which as acceptable given the average gross revenue of a show is $22 Million; and the model has a R2 of 0.985, indicating a high degree of fitness to the training dataset. The model is exported to Google Cloud Storage.

**Flask App Deployment and Testing**

A flask application is developed to serve out the prediction results. Flask is a lightweight micro web framework. It allows for applications to be called with requests to a particular web address. The user will enter 7 variables, as mentioned in previous section, including both numerical and strings, which can be chosen from a dropdown list. These variables are input to the trained model and a predicted gross revenue will be presented to the user.

The application is deployed to Google App Engine, and accessible at the following address: https://zhang-msds433.uc.r.appspot.com/. The log monitoring is also provided by GCP. A load test is performed using Apache Bench. 1000 requests were sent, with maximum simultaneous request of 100. All requests were successful, and the server can process on average 95 requests per second. The billing records are exported from Billing API in GCP to BigQuery, and a linear regression model is used to project the cost. Currently with minimal number of requests, the project bill is close to $0.

Continuous Integration is a critical development practice, in which developers commit and test code into a shared depository regularly and frequently. CI is adopted in the development process using GitHub Action, and commits are well annotated.

**Conclusion**

This application takes comprehensive history box office records for Broadway Shows, and provides prediction of gross revenue when crucial information such as time and place of performance is provided. The trained random forest model has a high degree of fitness, and the application served on Google App Engine allows stable and flexible traffic. Hopefully this web application will help the show production professionals to make decisions and the performance industry a healthy recovery from the financial impact of pandemic shutdowns.
