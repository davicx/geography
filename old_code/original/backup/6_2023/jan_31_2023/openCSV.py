import pandas as pd
import time

data = pd.read_csv('data/second.csv')

 
for index, row in data.iterrows():
    name = row['Second']
    print(name)
    time.sleep(4)
    

