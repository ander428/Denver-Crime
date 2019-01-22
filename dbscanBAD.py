# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 18:59:09 2019

@author: ericv
"""

#https://blog.dominodatalab.com/topology-and-density-based-clustering/

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

prob = pd.read_csv('C:/Users/ericv/Desktop/crimeprob.csv')
label = prob.values[::,0]
prob = prob.drop(['neighborhood'], axis=1)

data = prob[["arson", "murder"]]
data = data.values.astype("float32", copy = False)


stscaler = StandardScaler().fit(data)
data = stscaler.transform(data)
print(stscaler)