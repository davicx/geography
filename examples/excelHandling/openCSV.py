import pandas as pd
import time


#File Location: /Users/david/Desktop/David/www/geography/code/excelHandling/openCSV.py
data = pd.read_csv('/Users/david/Desktop/David/www/geography/code/excelHandling/excel/basinData.csv')

for index, row in data.iterrows():
    search_terms = row['search_terms']
    basin_code = row['basin_code']
    print(basin_code)
    print(search_terms)
    print(" ")

    time.sleep(1)
    
