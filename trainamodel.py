import pandas as pd
from sklearn import preprocessing

dataset = pd.read_csv('clean data.csv')
dataset.head()
Y=dataset['Gross']
enc = preprocessing.OrdinalEncoder()
X1=dataset.drop('Gross', axis=1)
enc.fit(X1)
X=enc.transform(X1)
print(Y)
#chose to use random forest regressor because it naturally handles catagorical variables.s
from sklearn.ensemble import RandomForestRegressor

rfr = RandomForestRegressor(n_estimators = 200)
rfr.fit(X, Y)

from sklearn import metrics
Y_true=Y.array
Y_pred = [rfr.predict(X)][0] # The predictions from your ML / RF model

print('Mean Absolute Error (MAE):', metrics.mean_absolute_error(Y_true, Y_pred))
print('R^2:', metrics.r2_score(Y_true, Y_pred))

import pickle
pickle.dump(enc,open("encoder.p", "wb"))
pickle.dump(rfr,open("model.p", "wb"))


# Mean Absolute Error (MAE): 1496360.629552941
# R^2: 0.9876097550943198