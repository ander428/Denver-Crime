# Matt Greenburg - 2255210
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
import zipfile
from FOM import FOM

''' DATA AQUISITION '''

# Unzip CSV file and create directory if not done already
csv_path = "./Data/CrimeCSV/"
csv_name = "crime.csv"
if not os.path.isdir(csv_path) and not os.path.exists(csv_path + csv_name):
    print("Extracting data...")
    zip_ref = zipfile.ZipFile("denver-crime-data.zip", 'r')
    zip_ref.extractall(csv_path)
    zip_ref.close()
    print("Done.")

# Read CSV into pandas DataFrame
print("Reading CSV file...")
df = pd.read_csv((csv_path + csv_name), delimiter=',', encoding="utf-8-sig")
print("Done.")

''' PREDICT OFFENSE CATEGORY BY NEIGHBORHOOD '''

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

# Train Crime Data
#   Parameters:
#       DataFrame - Contains REPORTED_DATE, NEIGHBORHOOD_ID, and OFFENSE_CATEGORY_ID
#       List - Consists of 2 column names for keys and values respectively
markov.learn(crimeByNID, ["NEIGHBORHOOD_ID", "OFFENSE_CATEGORY_ID"])

# Markov Crime Predicion
#   Parameters - Neighborhood, Crime
#   Output - Returns next predicted crime in the given neighborhood
prediction = markov.predict("cbd", "burglary") # example
print("Done.")

''' PREDICT NEIGHBORHOOD BY OFFENSE CATEGORY '''

# Changes to predicting neighborhood by offense category
# by switching the keys an values
print("Predicting Neighborhood by Offense Category...")
markov.learn(crimeByNID, ["OFFENSE_CATEGORY_ID", "NEIGHBORHOOD_ID"])
prediction = markov.predict("burglary", "cbd") # example
print("Done.")
