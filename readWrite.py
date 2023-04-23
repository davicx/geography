import pandas as pd
import time

data = pd.read_csv('data/readWrite.csv')

for index, row in data.iterrows():
    search_terms = row['basin']
    basin_code = row['to_do']
    print(basin_code)
    print(search_terms)
    print("")

    time.sleep(1)
    