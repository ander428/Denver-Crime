# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 16:15:58 2019

@author: green
"""
import numpy as np
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import pandas as pd

data = pd.read_csv('crimefigs.csv')
data
data = data[["arson", "burglary"]]
data = data.values.astype("float32", copy = False)

stscaler = StandardScaler().fit(data)
data = stscaler.transform(data)

plt.scatter(data[:,0], data[:,1])
plt.xlabel("Arson")
plt.ylabel("Burglary")
plt.title("Crime Data")

dbsc = DBSCAN(eps = .4, min_samples = 10).fit(data)

labels = dbsc.labels_
core_samples = np.zeros_like(labels, dtype = bool)
core_samples[dbsc.core_sample_indices_] = True

unique_labels = np.unique(labels)
colors = plt.cm.Spectral(np.linspace(0,1, len(unique_labels)))

for (label, color) in zip(unique_labels, colors):
    class_member_mask = (labels == label)
    xy = data[class_member_mask & core_samples]
    plt.plot(xy[:,0],xy[:,1], 'o', markerfacecolor = color, markersize = 10)
    
    xy2 = data[class_member_mask & ~core_samples]
    plt.plot(xy2[:,0],xy2[:,1], 'o', markerfacecolor = color, markersize = 5)
plt.title("DBSCAN on Crimes data")
plt.xlabel("Arson (scaled)")
plt.ylabel("Burglary (scaled)")