# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:01:29 2021

@author: ASUS
"""

#import pandas
import pandas as pd
#read csv file using pandas
data_set =pd.read_csv('loan_small.csv')
# Access the dataframe data using iloc
subset = data_set.iloc[0:3,1:3]
# another way of accessing the data from data frame using column names
subsetn= data_set[['Gender','ApplicantIncome']]
#read tsv file using pandas
data_setT =pd.read_csv('loan_small_tsv.txt',sep="\t")
#functions in pandas
#head- to get the quick review of the data set
data_set.head()
#shape to get number of rows and columns
data_set.shape
data_set.columns
#find out the columns with missing values
data_set.isnull().sum(axis=0)
#Data Pre-processing by replacing missing values in dataset
# drop/delete the cell with missing values 
clean_data = data_set.dropna(subset=['Loan_Status'])
#replace categorical data with mode
#copy the data set
dt= data_set.copy()
#replace numerical missing value
cols2=['ApplicantIncome','CoapplicantIncome','LoanAmount']
dt[cols2]=dt[cols2].astype('float')
print(dt.dtypes)
dt[cols2]=dt[cols2].fillna(dt.mean().iloc[0])
print(dt.isnull().sum(axis=0))
#replace categorical missing value
cols=['Gender','Area','Loan_Status']
dt[cols]=dt[cols].astype('category')
print(dt.dtypes)
dt[cols]=dt[cols].fillna(dt.mode().iloc[0])
#label encoding using python
print(dt.dtypes)
for columns in cols:
    dt[columns]=dt[columns].cat.codes
#hot encoding
dt=dt.drop(['Loan_ID'], axis=1)
dt=pd.get_dummies(dt, drop_first=(True))

