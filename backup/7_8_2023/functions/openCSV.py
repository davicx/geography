import pandas as pd
import time

data = pd.read_csv('data/secondLevelSearch.csv')

for index, row in data.iterrows():
    search_terms = row['search_terms']
    basin_code = row['basin_code']
    print(basin_code)
    print(search_terms)
    print("")

    time.sleep(1)
    

