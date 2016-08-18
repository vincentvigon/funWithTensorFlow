import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold   #For K-fold cross validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import metrics



'''https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-learn-data-science-python-scratch-2/'''

df = pd.read_csv("data/train.csv") #Reading the dataset in a dataframe using Pandas

#print(df.head(10))
#print(df.describe())
#print(df['Property_Area'].value_counts())
#df['ApplicantIncome'].hist(bins=50)
#df.boxplot(column='ApplicantIncome')
#df.boxplot(column='ApplicantIncome', by = 'Education')
#df.boxplot(column='LoanAmount')

#plt.show()



def crossTable():
    temp3 = pd.crosstab(df['Gender'], df['Loan_Status'])
    temp3.plot(kind='bar', stacked=True, color=['red', 'blue'], grid=False)
    plt.show()
    return

def pivotTable():
    temp1 = df['Credit_History'].value_counts(ascending=True)
    temp2 = df.pivot_table(values='Loan_Status', index=['Credit_History','Gender'],
                           aggfunc=lambda x: x.map({'Y': 1, 'N': 0}).mean())
    print('Frequency Table for Credit History:')
    print(temp1)

    print('\n Probability of getting loan for each Credit History class:')
    print(temp2)

    fig = plt.figure(figsize=(8, 4))
    ax1 = fig.add_subplot(121)
    ax1.set_xlabel('Credit_History')
    ax1.set_ylabel('Count of Applicants')
    ax1.set_title("Applicants by Credit_History")
    temp1.plot(kind='bar')

    ax2 = fig.add_subplot(122)
    temp2.plot(kind='bar')
    ax2.set_xlabel('Credit_History')
    ax2.set_ylabel('Probability of getting loan')
    ax2.set_title("Probability of getting loan by credit history")

    plt.show()

    return




from sklearn.preprocessing import LabelEncoder
var_mod = ['Gender']#,'Married','Dependents','Education','Self_Employed','Property_Area','Loan_Status']
le = LabelEncoder()
for i in var_mod:
    df[i] = le.fit_transform(df[i])
#print(df.dtypes)


#
# model=LogisticRegression()
# outcome = 'Loan_Status'
# predictors = ['Credit_History']
#
# #Fit the model:
# model.fit(df[predictors],df[outcome])
#
#
# #Make predictions on training set:
# predictions = model.predict(df[predictors])
#
# #Print accuracy
# accuracy = metrics.accuracy_score(predictions,df[outcome])
# print("Accuracy : %s" % "{0:.3%}".format(accuracy))


#print(df.apply(lambda x: sum(x.isnull()),axis=0))




