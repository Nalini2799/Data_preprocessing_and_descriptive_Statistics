# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 21:23:29 2021

@author: ASUS
"""

#Data processing in python- Test, Train and split 
#import pandas
import pandas as pd
#read csv file using pandas
data_set =pd.read_csv('loan_small.csv')
# drop/delete the cell with missing values 
clean_data = data_set.dropna(subset=['Loan_Status'])
#copy the data set
dt5= data_set.copy()
cols2=['ApplicantIncome','CoapplicantIncome','LoanAmount']
#change the datatype
dt5[cols2]=dt5[cols2].astype('float')
print(dt5.dtypes)
cols=['Gender','Area','Loan_Status']
dt5[cols]=dt5[cols].astype('category')
print(dt5.dtypes)
dt5[cols]=dt5[cols].fillna(dt5.mode().iloc[0])
print(dt5.isnull().sum(axis=0))
dt5[cols2]=dt5[cols2].fillna(dt5.mean().iloc[0])
print(dt5.isnull().sum(axis=0))
dt5=dt5.drop(['Loan_ID'], axis=1)
dt5=pd.get_dummies(dt5, drop_first=(True))
#split the data into vertically X and Y
X =dt5.iloc[:,:-1]
#fetch all the column except the last one
Y =dt5.iloc[:,-1]
#fetch only the last column
#split the data set by rows/horizontally
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test =\
    train_test_split(X,Y,test_size=0.2,random_state=1234)




