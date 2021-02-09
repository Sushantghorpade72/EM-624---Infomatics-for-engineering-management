# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:52:33 2020

@author: Sushant
"""
#importing pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import BernoulliNB


#load our data file
df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
#print number of rows and columns
print('\n--->There are',df.shape[0],'rows and',df.shape[1],'columns in our dataset\n')
#print first 5 observation
print('--->First 5 observations:\n\n',df.head())
#print informationon data
print('\n--->Above is description of variables\n\n',df.info())
#Print stastical infornation on our variables
print('\n--->Stastical information on our variables\n\n',df.describe())

#Exploratory Data Analysis/Visualization
sns.set_style('darkgrid')
#Create count plot on"Attrition" w.r.t Gender distribution in our dataset
plt.title('"Attrition" w.r.t Gender ')
plt.legend()
sns.countplot(df['Attrition'],hue= df['Gender'] )

#Creating pie chart
plt.figure(figsize=(10,6))
plt.pie(df['Department'].value_counts(),labels=['Research & Development','Sales','Human Resources'],autopct='%1.1f%%')
plt.title("Population distribution through out depatments")

#Create count plot for numaber of males and females based on department in our dataset
plt.figure(figsize=(10,6))
plt.title('Employee distribution through out depatments w.r.t gender')
sns.countplot(x='Department',hue='Gender',data=df,palette='Set1')

#Create histogram to see 'Age distribution w.r.t gender'
#For Gender ('Male': 1,'Female' : 0)
Gen = {'Male': 1,'Female' : 0}
df['Gender'] = df['Gender'].map(Gen)
df[df['Gender']==1]['Age'].hist(alpha=0.45,color='blue',bins=40,label='Male')
df[df['Gender']==0]['Age'].hist(alpha=0.45,color='red',bins=40,label='Female')
plt.legend()
plt.title('Age distribution w.r.t gender')
plt.xlabel('Age')
plt.ylabel('Frequency')

#Find relation between Age and Income
plt.figure(figsize=(16,16))
sns.lmplot(y='MonthlyIncome',x='Age',data=df,hue='Gender',col='Department',palette='Set1')

plt.figure(figsize=(12,6))
plt.title('Number of people working with current manager w.r.t years')
sns.countplot(df['YearsWithCurrManager'])

#Print correlation plot to find relationship between variables
plt.figure(figsize=(16,16))
sns.heatmap(df.corr(),annot= True,linewidths=0.5,linecolor='black')

#--------------------------------Using Classifier to classify wheather given employee will fall under attrition or not-------------------#
print('\n-----Using machine learning to classify wheather given employee will fall under attrition or not----\n')
print('\n---Data preparation---\n')
#Numeric encoding variables
# for Over18 and Overtime (1 = 'Y', 0 = 'N')
O_18 = {'Y': 1,'N' : 0}
df['Over18'] = df['Over18'].map(O_18)

# for Overtime (1 = 'Yes', 0 = 'N0')
OT = {'Yes': 1,'No' : 0}
df['OverTime'] = df['OverTime'].map(OT)

#segregate catagorical columns data form numeric
cat_data = []

for col,val in df.iteritems():
    if val.dtype == 'object':
        cat_data.append(col)
print(cat_data)  

#store it in our dataframe
df_cat = df[cat_data]
df_cat = df_cat.drop(['Attrition'], axis=1)

#segregate target variable
#For Attrition ('Yes':1,'No':0)
attrate = {'Yes':1, 'No':0}

# Use the pandas apply method to numerically encode our attrition target variable
target = df['Attrition'].map(attrate)
target.head(3)

#seprate for numeric data
num_data = df.columns.difference(cat_data)
#store numeric data in dataframe
df_num = df[num_data]

#Creating dummy variables catagorical data for onehot encoding
df_dummy_cat = pd.get_dummies(data=df_cat)
print('\n--->There are',df_dummy_cat.shape[0],'rows and',df_dummy_cat.shape[1],'columns in our dataset\n')

#Concat numeric and dummy vars data to single dataframe
df_final = pd.concat([df_num, df_dummy_cat], axis=1)
print('\n--->There are',df_final.shape[0],'rows and',df_final.shape[1],'columns in our dataset\n')
print('--->First 5 observations:\n\n',df_final.head())

#Correlation plot after dummy variables
plt.figure(figsize=(16,16))
sns.heatmap(df_final.corr(),linewidths=0.5,linecolor='black')

print('---Modeling and Evaluation---')
#define dependent and independent variables
X = df_final
y = target
#Split data into train and test dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state= 101)

print('---Using logistic Regression---')
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)
log_predictions = logmodel.predict(X_test)
print('\nPrint results for our logestic regression model\n')
print('--->Classification report\n\n',classification_report(y_test,log_predictions))
print('\n--->Confusion Matrix\n\n',confusion_matrix(y_test,log_predictions))

print('---Using Decision Tree---')
dtc = DecisionTreeClassifier()
dtc.fit(X_train,y_train)
dtc_predictions = dtc.predict(X_test)
print('\nPrint results for our Decision tree classifier model\n')
print('--->Classification report\n\n',classification_report(y_test,dtc_predictions))
print('\n--->Confusion Matrix\n\n',confusion_matrix(y_test,dtc_predictions))

print('---Using RandomForest---')
rfc = RandomForestClassifier()
rfc.fit(X_train,y_train)
rfc_predictions = rfc.predict(X_test)
print('\nPrint results for our RandomForest classifier model\n')
print('--->Classification report\n\n',classification_report(y_test,rfc_predictions))
print('\n--->Confusion Matrix\n\n',confusion_matrix(y_test,rfc_predictions))

print('---Using Naive Bayes---')
bnb = BernoulliNB()
bnb.fit(X_train,y_train)
bnb_predictions = bnb.predict(X_test)
print('\nPrint results for our Naive Bayes classifier model\n')
print('--->Classification report\n\n',classification_report(y_test,bnb_predictions))
print('\n--->Confusion Matrix\n\n',confusion_matrix(y_test,bnb_predictions))



