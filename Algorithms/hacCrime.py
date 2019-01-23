# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 12:16:42 2019

@author: green
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cluster
import scipy.cluster.hierarchy as shc

#prob = pd.read_csv('crimefigsClean.csv')
#label = list(prob.columns.values)
#prob = prob.transpose()
##prob = prob.drop(['neighborhood'], axis=1)
#
##set up plot dendogram plot
#plt.figure(figsize=(12, 8))
#plt.title("Dendrogram")
#dend = shc.dendrogram(shc.linkage(prob, method='ward'), labels = label)
#plt.figure(figsize=(12, 8))
#dend = shc.dendrogram(shc.linkage(prob, method='complete'), labels = label)

#Examines the uniqueness of certain crimes and how they appear together in certain neighborhoods
prob = pd.read_csv('../CSVs/crimefigs.csv')
prob = prob.transpose()
prob = prob.drop(['neighborhood'])
label = prob.index

#set up plot dendogram plot
plt.figure(figsize=(12, 8))
plt.title("Dendrogram")
dend = shc.dendrogram(shc.linkage(prob, method='ward'), labels = label, leaf_rotation = 90, leaf_font_size = 11)
plt.figure(figsize=(12, 8))
dend = shc.dendrogram(shc.linkage(prob, method='complete'), labels = label, leaf_rotation = 90, leaf_font_size = 11)
