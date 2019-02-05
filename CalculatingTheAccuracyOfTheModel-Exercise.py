import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sn
from threading import Thread
from time import sleep
sn.set()


raw_data = pd.read_csv('D:\Springmobile Backup\Google Drive\Data Science\Binary Predictors-accuracy\Bank-data-accuracy.csv')
print(raw_data)
data = raw_data.copy()
# Remove the index column that comes with the data
data = data.drop(['Unnamed: 0'], axis=1)
# Now Map the data so that Yes values map to 1 and No values map to 0
data['y'] = data['y'].map({'yes': 1, 'no': 0})

x1 = data['duration']
y = data['y']

x = sm.add_constant(x1)
reg_log = sm.Logit(y, x)
results_log = reg_log.fit()
print(results_log.summary())

plt.scatter(x1,y, color='C0')
plt.xlabel('Duration')
plt.ylabel('Subscription')
plt.show()

estimators = ['interest_rate','march','credit','previous','duration']
X = data[estimators]
y = data['y']

reg_logit = sm.Logit(y,X)
results_logit = reg_logit.fit()
print(results_logit.summary2())

def confusion_matrix(data, actual_values, model):

    #Parameters
    # ----------
    #data: data frame or array
    #data is a data frame formatted in the same way as your input data (without the actual values)
    # e.g. const, var1, var2, etc. Order is very important!
    # actual_values: data frame or array
    # These are the actual values from the test_data
    # In the case of a logistic regression, it should be a single column with 0s and 1s

    # model: a LogitResults object
    # this is the variable where you have the fitted model
    # e.g. results_log in this course
    # ----------

    #predict the values using the logit model

    pred_values = model.predict(data)
    # specify the bins
    bins = np.array([0,0.5,1])
    # Create a histogram, where if values are between 0 and 0.5 tell will be considered 0
    # if they are between 0.5 and 1, they will be considered 1
    cm = np.histogram2d(actual_values, pred_values, bins=bins)[0]
    accuracy = (cm[0,0] + cm[1,1])/cm.sum()
    return cm,accuracy




print(confusion_matrix(X,y,results_logit))
