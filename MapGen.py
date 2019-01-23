# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:06:52 2019

@author: green
"""
import pandas as pd
import matplotlib.pyplot as plt
from DenverMap import DenverMap
import numpy

df = pd.read_csv('MapData.csv')
long = df['GEO_LON']
lat = df['GEO_LAT']

map = DenverMap()
x, y = map.getMap()(long.tolist(), lat.tolist())
map.plot(x,y)
map.show()
