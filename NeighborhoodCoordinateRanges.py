#https://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
import os
import zipfile

#csv_path = "./Data/CrimeCSV/"
#csv_name = "crime.csv"
#if not os.path.isdir(csv_path) and not os.path.exists(csv_path + csv_name):
#    print("Extracting data...")
#    zip_ref = zipfile.ZipFile("denver-crime-data.zip", 'r')
#    zip_ref.extractall(csv_path)
#    zip_ref.close()
#    print("Done.")
#
## Read CSV into pandas DataFrame
#print("Reading CSV file...")
#df = pd.read_csv((csv_path + csv_name), delimiter=',', encoding="utf-8-sig")
#print("Done.")

## iterate through every row in DataFrame
subset_df = df[["NEIGHBORHOOD_ID" , "GEO_LAT", "GEO_LON"]].copy()
#a = subset_df[subset_df.groupby('NEIGHBORHOOD_ID')['GEO_LAT'].transform(min) == subset_df['GEO_LAT']]
#print(a)
min_lat = subset_df.sort_values(by=['GEO_LAT']).drop_duplicates(['NEIGHBORHOOD_ID'], keep='first')
min_long = subset_df.sort_values(by=['GEO_LAT']).drop_duplicates(['NEIGHBORHOOD_ID'], keep='first')
print(min_lat)
#min_lat = subset_df.groupby('NEIGHBORHOOD_ID')['GEO_LAT'].min()[subset_df['NEIGHBORHOOD_ID']]
#print(min_lat)
#
#min_lat.reset_index(drop = True, inplace = True)
#min_lat_index = subset_df.groupby('NEIGHBORHOOD_ID')['GEO_LAT'].idxmin()[subset_df['GEO_LAT']]

#print(min_lat)

min_lon = subset_df.groupby('NEIGHBORHOOD_ID')['GEO_LAT'].min()[subset_df['NEIGHBORHOOD_ID']]

print(subset_df.NEIGHBORHOOD_ID.unique())

#dictionary = {}
#for i, row in enumerate(subset_df.iterrows()):
#    row = row[1]
#    if row["NEIGHBORHOOD_ID"] not in dictionary.keys():
#        dictionary[row["NEIGHBORHOOD_ID"]] = [row[["GEO_LAT", "GEO_LON"]]]
    