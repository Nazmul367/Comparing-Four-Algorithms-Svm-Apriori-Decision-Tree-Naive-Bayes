# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 09:11:44 2018

@author: Nazmul_367
"""

import numpy as np
from sklearn import  svm
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv('Market_Basket_Optimisation.csv', header=None)

transactions=[]
for i in range(0,7501):
    transactions.append([str(df.values[i,j]) for j in range (0,20)])

from apyori import apriori
rules=apriori(transactions,min_support=.003, min_confidence=0.4, min_lift=3, min_length=2)

anss=list(rules)

print(anss)