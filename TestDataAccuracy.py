import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sn
sn.set()
raw_data = pd.read_csv('D:\Springmobile Backup\Google Drive\Data Science\TestDataSet\\2.02. Binary predictors.csv')

data = raw_data.copy()
data['Admitted'] = data['Admitted'].map({'Yes': 1, 'No': 0})
data['Gender'] = data['Gender'].map({'Female': 1, 'Male': 0})
print(data)
# Declare the dependant and independant variables

y = data['Admitted']
x1 = data[['SAT','Gender']]

x = sm.add_constant(x1)
reg_log = sm.Logit(y,x)
results_log = reg_log.fit()
print(results_log.summary())
print(np.exp(1.9449))

#Accuracy
np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
print(results_log.predict())
print(np.array(data['Admitted']))
print(results_log.pred_table())


test= pd.read_csv('D:\Springmobile Backup\Google Drive\Data Science\TestDataSet\\2.03. Test dataset.csv')

test['Admitted'] = test['Admitted'].map({'Yes': 1, 'No': 0})

test['Gender'] = test['Gender'].map({'Female':1, 'Male': 0})
# what we will be doing is
# 1. We will use our model to make predictions based on the test data
# 2. We will compare those with the actual outcome
# 3. Calculate the accuracy
# 4. Create a confusion matrix

print(x)  # Order is very important i.e., Const, SAT, Geneder, because the coefficients of the regression with expect it

test_actual = test['Admitted']
test_data = test.drop(['Admitted'], axis =1)
test_data= sm.add_constant(test_data)
print(test_data)


def confusion_matrix(data, actual_values, model):
    pred_values = model.predict(data)
    bins = np.array([0,0.5,1])
    cm = np.histogram2d(actual_values, pred_values, bins=bins)[0]
    accuracy = (cm[0,0] + cm[1,1])/cm.sum()
    return cm, accuracy

cm = confusion_matrix(test_data, test_actual, results_log)
print(cm)

cm_df = pd.DataFrame(cm[0])
print(cm_df)
cm_df.columns = ['Predicted 0', 'Predicted 1']
print(cm_df)
cm_df = cm_df.rename(index={0: 'Actual 0', 1: 'Actual 1'})
print(cm_df)
print('Misclassification rate: ' + str((1+1)/19))
