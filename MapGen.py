# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:06:52 2019

@author: green
"""
import pandas as pd
import matplotlib.pyplot as plt
from DenverMap import DenverMap
import numpy

df = pd.read_csv('./CSVs/MapData.csv')
crimes = df[["GEO_LON", "GEO_LAT" , "OFFENSE_CATEGORY_ID"]].copy()

crimes = crimes.loc[crimes['OFFENSE_CATEGORY_ID'] == "white-collar-crime"]

long = crimes['GEO_LON']
lat = crimes['GEO_LAT']

map = DenverMap()

for row in crimes.iterrows():
    row = row[1]
    x, y = map.getMap()(row["GEO_LON"], row["GEO_LAT"])
    map.plot(x,y)
map.show()
