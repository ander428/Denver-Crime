#https://blog.dominodatalab.com/topology-and-density-based-clustering/

import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc

prob = pd.read_csv('crimeprob.csv')
label = prob.values[::,0]
prob = prob.drop(['neighborhood'], axis=1)

#set up plot dendogram plot
plt.figure(figsize=(12, 8))  
plt.title("Dendrogram")  
dend = shc.dendrogram(shc.linkage(prob, method='ward'), labels = label)
plt.figure(figsize=(12, 8))  
dend = shc.dendrogram(shc.linkage(prob, method='complete'), labels = label) 
