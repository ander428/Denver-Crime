# Matt Greenberg - 2255210
# Joshua Anderson - 2270306
# Eric Vela - 2277759
#
# This program takes in a csv file containing crime data in Denver
# and returns analytics from DBSCAN, Markov, and HAC Algorithms
#
# DBSCAN - Density of Crimes based on Location or Neighborhood
# Markov - Predict a Crime to occur in a certain Location
# HAC - Associate crime frequency with Neighborhood

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import zipfile
from Algorithms.FOM import FOM
from DenverMap import DenverMap
import threading

''' DATA AQUISITION '''

# Unzip CSV file and create directory if not done already
csv_path = "./CSVs/CrimeCSV/"
csv_name = "crime.csv"
if not os.path.isdir(csv_path) and not os.path.exists(csv_path + csv_name):
    print("Extracting data...")
    zip_ref = zipfile.ZipFile("denver-crime-data.zip", 'r')
    zip_ref.extractall(csv_path)
    zip_ref.close()
    print("Done.")

# Read CSV into pandas DataFrame
print("Reading CSV file...")
data = pd.read_csv((csv_path + csv_name), delimiter=',', encoding="utf-8-sig")
print("Done.")

''' PREDICT OFFENSE CATEGORY BY NEIGHBORHOOD '''
def runMarkov(df):
    # Create subset of crimes containing only REPORTED_DATE, NEIGHBORHOOD_ID, and OFFENSE_CATEGORY_ID
    print("Loading Data for Markov...")
    crimeByNID = df[["REPORTED_DATE", "NEIGHBORHOOD_ID" , "OFFENSE_CATEGORY_ID"]].copy()
    crimeByNID.loc[:,"REPORTED_DATE"] = pd.to_datetime(crimeByNID.loc[:,"REPORTED_DATE"])
    crimeByNID.set_index('REPORTED_DATE', drop=True, append=False, inplace=True, verify_integrity=False)
    crimeByNID = crimeByNID.sort_index()
    print("Done.")

    # Initialize and train First Order Markov Model
    print("Predicting Offense Category by Neighborhood...")
    markov = FOM()

    # Train Crime Datav
    #   Parameters:
    #       DataFrame - Contains REPORTED_DATE, NEIGHBORHOOD_ID, and OFFENSE_CATEGORY_ID
    #       List - Consists of 2 column names for keys and values respectively
    print("Training Data...")
    markov.learn(crimeByNID, ["NEIGHBORHOOD_ID", "OFFENSE_CATEGORY_ID"])
    print("Done.")
    # Markov Crime Predicion
    #   Parameters - Neighborhood, Crime
    #   Output - Returns next predicted crime in the given neighborhood
    print("Predicting...")
    predictions = {}
    for neighborhood, crimes in markov.getMemory().items():
        lastCrime = crimes[len(crimes)-1]
        pred = markov.predict(neighborhood, lastCrime)
        predictions[neighborhood] = pred
    print("Predicted Crimes by Neighborhood:")

    f = open("MarkovPredictions.txt", 'w')
    for key, value in predictions.items():
        line = str(key) + ": " + str(value) + "\n"
        f.write(line)
    f.close()
    print("Done.")

    ''' PREDICT NEIGHBORHOOD BY OFFENSE CATEGORY '''

    # Changes to predicting neighborhood by offense category
    # by switching the keys an values
    print("Predicting Neighborhood by Offense Category...")
    markov.learn(crimeByNID, ["OFFENSE_CATEGORY_ID", "NEIGHBORHOOD_ID"])
    prediction = markov.predict("burglary", "cbd") # example
    print("Done.")


''' PLOTTING DENSITY OF CRIMES ON MAP '''
# Source: https://stackoverflow.com/questions/11507575/basemap-and-density-plots
def showDensity():
    print("Plotting Density Map...")
    df = pd.read_csv('./CSVs/MapData.csv')
    lons = df['GEO_LON']
    lats = df['GEO_LAT']

    nx, ny = 18, 7
    map = DenverMap()

    # compute appropriate bins to histogram the data into
    lon_bins = np.linspace(lons.min(), lons.max(), nx+1)
    lat_bins = np.linspace(lats.min(), lats.max(), ny+1)

    # Histogram the lats and lons to produce an array of frequencies in each box.
    # Because histogram2d does not follow the cartesian convention
    # (as documented in the numpy.histogram2d docs)
    # we need to provide lats and lons rather than lons and lats
    density, _, _ = np.histogram2d(lats, lons, [lat_bins, lon_bins])

    # Turn the lon/lat bins into 2 dimensional arrays ready
    # for conversion into projected coordinates
    lon_bins_2d, lat_bins_2d = np.meshgrid(lon_bins, lat_bins)

    # convert the xs and ys to map coordinates
    xs, ys = map.getMap()(lon_bins_2d, lat_bins_2d)

    plt.pcolormesh(xs, ys, density)
    plt.colorbar(orientation='horizontal')
    print("Done.")
    map.show()

''' PLOT ALL INSTANCES OF A GIVEN CRIME '''
def plotCrime(crime):
    df = pd.read_csv('./CSVs/MapData.csv')
    crimes = df[["GEO_LON", "GEO_LAT" , "OFFENSE_CATEGORY_ID"]].copy()

    crimes = crimes.loc[crimes['OFFENSE_CATEGORY_ID'] == crime]

    long = crimes['GEO_LON']
    lat = crimes['GEO_LAT']

    map = DenverMap()

    for row in crimes.iterrows():
        row = row[1]
        x, y = map.getMap()(row["GEO_LON"], row["GEO_LAT"])
        map.plot(x,y)
    map.show()

t1 = threading.Thread(target=runMarkov, args=(data,))
t1.start()
showDensity()
plotCrime("white-collar-crime")
