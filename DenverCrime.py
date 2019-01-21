import pandas as pd
import zipfile
from FOM import FOM

zip_ref = zipfile.ZipFile("denver-crime-data.zip", 'r')
zip_ref.extractall("./Data/CrimeCSV")
zip_ref.close()

df = pd.read_csv("./Data/CrimeCSV/crime.csv", delimiter=',', encoding="utf-8-sig")

df2 = df[["REPORTED_DATE", "NEIGHBORHOOD_ID" , "OFFENSE_CATEGORY_ID"]].copy()
df2.loc[:,"REPORTED_DATE"] = pd.to_datetime(df2.loc[:,"REPORTED_DATE"])
df2.set_index('REPORTED_DATE', drop=True, append=False, inplace=True, verify_integrity=False)
df2 = df2.sort_index()

markov = FOM()
markov.learn(df2, ["NEIGHBORHOOD_ID", "OFFENSE_CATEGORY_ID"])
pred = markov.choose() # returns dict of predictions for each neighborhood
