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
lons = df['GEO_LON']
lats = df['GEO_LAT']

nx, ny = 18, 7

map = DenverMap()
# x, y = map.getMap()(long.tolist(), lat.tolist())
# map.plot(x,y)

# compute appropriate bins to histogram the data into
lon_bins = numpy.linspace(lons.min(), lons.max(), nx+1)
lat_bins = numpy.linspace(lats.min(), lats.max(), ny+1)

# Histogram the lats and lons to produce an array of frequencies in each box.
# Because histogram2d does not follow the cartesian convention
# (as documented in the numpy.histogram2d docs)
# we need to provide lats and lons rather than lons and lats
density, _, _ = numpy.histogram2d(lats, lons, [lat_bins, lon_bins])

# Turn the lon/lat bins into 2 dimensional arrays ready
# for conversion into projected coordinates
lon_bins_2d, lat_bins_2d = numpy.meshgrid(lon_bins, lat_bins)

# convert the xs and ys to map coordinates
xs, ys = map.getMap()(lon_bins_2d, lat_bins_2d)

plt.pcolormesh(xs, ys, density)
plt.colorbar(orientation='horizontal')

map.show()
