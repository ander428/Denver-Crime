# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:06:52 2019

@author: green
"""
import pandas as pd
import matplotlib.pyplot as plt
from DenverMap import DenverMap

df = pd.read_csv('MapData.csv')

#df[['GEO_LON', 'GEO_LAT']]
x = df['GEO_LON']
y = df['GEO_LAT']
plt.scatter(x, y)
plt.show()

map = DenverMap()
map.show()