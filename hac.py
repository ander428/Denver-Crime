# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 19:46:37 2019

@author: ericv
"""
#can we substitute the states as neighborhoods
#each column is the percentage of each crime happening


import pandas as pd
import zipfile
from sklearn import cluster
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc

zip_ref = zipfile.ZipFile("denver-crime-data.zip", 'r')
zip_ref.extractall("./Data/CrimeCSV")
zip_ref.close()

#df = pd.read_csv("./Data/CrimeCSV/crime.csv", delimiter=',', encoding="utf-8-sig")
#df2 = df[["REPORTED_DATE", "NEIGHBORHOOD_ID" , "OFFENSE_CATEGORY_ID"]].copy()
#df2.loc[:,"REPORTED_DATE"] = pd.to_datetime(df2.loc[:,"REPORTED_DATE"])
#df2.set_index('REPORTED_DATE', drop=True, append=False, inplace=True, verify_integrity=False)
#df2 = df2.sort_index()

count = len(df2)
print(count)
    
#
##set up plot dendogram plot
#plt.figure(figsize=(12, 8))  
#plt.title("Dendrogram")  
#plt.xlabel("Neighborhood")
#dend = shc.dendrogram(shc.linkage(df2, method='single'))
#
##output gave us 3 clusters
##use this as a parameter
##loosely referenced https://stackabuse.com/hierarchical-clustering-with-python-and-scikit-learn/
#single = cluster.AgglomerativeClustering(n_clusters=3, linkage='single')
#single.fit_predict(df2)
#
##plot single agglomerative clustering
#plt.figure(figsize=(12, 8))  
#plt.scatter(df2[:,0],df2[:,1], c=single.labels_, cmap='rainbow') 