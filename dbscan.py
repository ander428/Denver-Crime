# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 18:59:09 2019

@author: ericv
"""

#https://blog.dominodatalab.com/topology-and-density-based-clustering/

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cluster
import scipy.cluster.hierarchy as shc

prob = pd.read_csv('C:/Users/ericv/Desktop/crimeprob.csv')
label = prob.values[::,0]
prob = prob.drop(['neighborhood'], axis=1)

#set up plot dendogram plot
plt.figure(figsize=(12, 8))  
plt.title("Dendrogram")  
dend = shc.dendrogram(shc.linkage(prob, method='complete'), labels = label)
