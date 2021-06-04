# -*- coding: utf-8 -*-
#import pandas
import pandas as pd
#read csv file using pandas
data_set =pd.read_csv('loan_small.csv')
#drops the rows with missing element
cleandata =data_set.dropna()
#extract the numerical data column
data_to_scale=cleandata.iloc[:,2:5]
#import standard scaler to perform normalisation
from sklearn.preprocessing import StandardScaler
scaler_s = StandardScaler()
ss= scaler_s.fit_transform(data_to_scale)
#min_max scaler
from sklearn.preprocessing import minmax_scale
mm = minmax_scale(data_to_scale)


