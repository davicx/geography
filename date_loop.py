from calendar import monthrange

import pandas as pd
import time

#FIRST MAJOR PART
#Step 1: Open aral.csv in status folder 
#Step 2: Loop over period of time to start to five years 2018 to 2023
#Step #: Update aral.csv in status folder 

#Fake data
#year - results 
#2018 - 900 
#2019 - 800
#2020 - 750
#2021 - 1100
#2022 - 700
#2023 - 800

#First loop over and print each year and the results
#Second Write this to a CSC file aral.csv
#start 2018 #stop 2018

'''
if under 1000 write done to excel 
else over 1000 write to excel not done 
'''

#Point to file in status folder 
#data = status/aral.csv
#data = pd.read_csv('/Users/david/Desktop/David/www/geography/code/excelHandling/excel/updateExcel.csv', index_col=0)
#data = pd.read_csv('/Users/dvas22/Desktop/David/www/geography/examples/excelHandling/excel/updateExcel.csv', index_col=0)


#Get the total days in a month 
def write_to_excel():
    for index, row in data.iterrows():
        basin = row['basin']
        start_date = row['start_date']
        end_date = row['end_date']
        finished = row['finished']

        if finished != 1:
            print("The data was downloaded marking complete")
            update_status(index)
            time.sleep(1)
        else:     
            print("The basin ", basin, " from ", start_date, " to ", end_date, " is already done so we are skipping")
            time.sleep(1)

def update_status(index):
    data.loc[index, ['finished']] = [1]
    df = pd.DataFrame(data)  
    df.to_csv('/Users/dvas22/Desktop/David/www/geography/examples/excelHandling/excel/updateExcel.csv')



#SECOND MAJOR PART
#Loop by full time, ten years, year, month, week date

#loop over any year 
def loop_over_year(year):
    for month in range(1, 13):
        #print("Loop ", year, month)
        date_range = monthrange(year, month)
        print("month number: ",  month, " " , date_range[1])

    #Simple Get days in a month 
    date_range = monthrange(2011, 2)
    #print(date_range[0])
    #print(date_range[1])
    #print(" ")
    date_range = monthrange(2023, 9)
    #print(date_range[0])
    #print(date_range[1])
    #print(" ")

loop_over_year(2023)

