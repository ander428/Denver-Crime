
import pandas as pd

df = pd.read_csv("C:/Users/ericv/Desktop/crime.csv", delimiter=',', encoding="utf-8-sig")


df2 = df[["REPORTED_DATE", "NEIGHBORHOOD_ID" , "OFFENSE_CATEGORY_ID"]].copy()
df2.loc[:,"REPORTED_DATE"] = pd.to_datetime(df2.loc[:,"REPORTED_DATE"])
df2.set_index('REPORTED_DATE', drop=True, append=False, inplace=True, verify_integrity=False)
df2 = df2.sort_index()
