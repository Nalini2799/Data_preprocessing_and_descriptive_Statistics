# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 17:59:17 2021

@author: ASUS
"""

#open files
import pandas as pd
mydataset = pd.read_csv('statistics.csv')
f = open("statistics.csv")
d = f.readlines()
t =map(float,d)
import statistics as st
mean =st.mean(t)
median =st.median(d)
u =map(float,d)
st_dev =st.stdev(u)
a =map(float,d)
var_1 =st.variance(a)
