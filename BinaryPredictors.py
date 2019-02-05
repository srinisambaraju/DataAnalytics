import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

raw_data = pd.read_csv('D:\Springmobile Backup\Google Drive\Data Science\\2.8. Binary predictors\\2.02. Binary predictors.csv')
print(raw_data.describe())
data = raw_data.copy()
data['Admitted'] = data['Admitted'].map({'Yes': 1, 'No': 0})
data['Gender'] = data['Gender'].map({'Female': 1, 'Male': 0})
print(data)

y = data['Admitted']
x1 = data['Gender']

x = sm.add_constant(x1)
reg_log = sm.Logit(y, x)
results_log = reg_log.fit()
print(results_log.summary())

# once the results summary is displayed, we can see that the model is significant because the LLR-pvalue is very high
# Gender value is significant i.e., p>|z| is 0.000 so the model is defined as
# log (odds) = -0.6436 + 2.0786 * Gender

# to interpret more take 2 equations log (odds2 ) and log (odds1)
# log(odds2) = -0.6436 + 2.0786 * Gender2
# log(odds1) = -0.6436 + 2.0786 * Gender1
# log (odds2 / odds1) = 2.0786 (Gender2 - Gender1)
# Gender is only 2 possible values so there is only a unit change there, so let Gender2 to be equal to 1 and Gender1
# equal to be 0, we know from our data that 1 is Female and 0 is male
# odds2 are the odds of getting female to get admitted and odds1 are odds of getting a male to get admitted
# so taking the log (odds2/odds1) = 2.08 * 1 which is 2.08, so taking exponential on both sides
print(np.exp(2.0786))
# the above value tells us the females are 7.99 time likely to get admitted than males


# We know that there is a strong relationship between SAT score and admittance

y = data['Admitted']
x1 = data[['SAT', 'Gender']]

x = sm.add_constant(x1)
reg_log = sm.Logit(y, x)
results_log = reg_log.fit()
print(results_log.summary())

# This time when you look at the summary you see the regression has a much higher log-likelihood than before
# -20.180 to -96.140 which tells this model fits the data very well
# We also see that gender value is significant which is 0.022 but we no longer see 0.000 like we did in the first time
# the new coefficient of gender is 1.94 and exponential of gender
print(np.exp(1.9449))  # 6.99

# Given the same SAT score , a female has 7 times higher odds to get admitted
# we should always look into it more details like may be in this particular university (degree) it is much easier
# for females to enter

