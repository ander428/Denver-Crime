#https://blog.dominodatalab.com/topology-and-density-based-clustering/

import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc

prob = pd.read_csv('../CSVs/crimeprob.csv')
label = prob.values[::,0]
prob = prob.drop(['neighborhood'], axis=1)

#set up plot dendogram plot
plt.figure(figsize=(12, 8))
plt.title("Dendrogram using Ward Linkage (Crime Probabilities)")
dend = shc.dendrogram(shc.linkage(prob, method='ward'), labels = label, leaf_font_size = 11)
plt.figure(figsize=(12, 8))
plt.title("Dendrogram using Complete Linkage (Crime Probabilities)")
dend = shc.dendrogram(shc.linkage(prob, method='complete'), labels = label, leaf_font_size = 11)

fig = pd.read_csv('../CSVs/crimefigs.csv')
label = fig.values[::,0]
fig = fig.drop(['neighborhood'], axis=1)

#set up plot dendogram plot
plt.figure(figsize=(12, 8))
plt.title("Dendrogram using Ward Linkage (Crime Figures)")
dend = shc.dendrogram(shc.linkage(fig, method='ward'), labels = label, leaf_font_size = 11)
plt.figure(figsize=(12, 8))
plt.title("Dendrogram using Complete Linkage (Crime Figures)")
dend = shc.dendrogram(shc.linkage(fig, method='complete'), labels = label, leaf_font_size = 11)