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
subset_df = df[["NEIGHBORHOOD_ID" , "OFFENSE_CATEGORY_ID"]].copy()
items = subset_df.values.tolist()
 
te = TransactionEncoder()
te_ary = te.fit(items).transform(items)
bool_df = pd.DataFrame(te_ary, columns=te.columns_)

ap = apriori(bool_df, min_support=0.17,use_colnames=True)
print(ap)