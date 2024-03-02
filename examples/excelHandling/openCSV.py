import pandas as pd
import time


#File Location: /Users/david/Desktop/David/www/geography/code/excelHandling/openCSV.py
#data = pd.read_csv('/Users/david/Desktop/David/www/geography/code/excelHandling/excel/basinData.csv')
#data = pd.read_csv('/Users/dvas22/Desktop/David/www/geography/examples/excelHandling/excel/basinData.py')
#data = pd.read_csv('/Users/dvas22/Desktop/David/www/geography/examples/excelHandling/excel/basinData.csv')
#File Location PC: c:\Users\Melissa\Documents\EventsAutomation\geography\examples\excelHandling\excel\basinData.csv

data = pd.read_csv('C:/Users/Melissa/Documents/EventsAutomation/geography/examples/excelHandling/excel/basinData.csv')

for index, row in data.iterrows():
    search_terms = row['search_terms']
    basin_code = row['basin_code']
    print(basin_code)
    print(search_terms)
    print(" ")

    time.sleep(1)
    

