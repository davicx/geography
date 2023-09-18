from calendar import monthrange

import pandas as pd
import time

#TO DO
#PART 1: Get Login to Work for Tufts
#PART 2: Change the Set Sort by to Date (oldest to Newest)
#PART 3: Simple Read and Write to Excel
#PART 4: Create Date Loop Functions that work by year, month, day and week (do this last I think its tricky)

#INSTRUCTIONS 
#PART 1 and PART 2: These are what you have been doing if you have any questions let me know! 

#PART 3: Simple Read and Write to Excel
'''
Part 3A
Try to read data from an excel file code example: 
/Users/dvas22/Desktop/David/www/geography/examples/excelHandling/openCSV.py

Part 3B
Try to update the excel file 
/Users/dvas22/Desktop/David/www/geography/examples/excelHandling/excel/updateExcel.csv
There is an example of this code here:
/Users/dvas22/Desktop/David/www/geography/examples/excelHandling/updateExcel.py
'''

#PART 4: Create Date Loop Functions that work by year, month, day and week
#Search runs from 30 June 2008 and 1 July 2023 and date is formatted "02/01/2011"

#Example Loop by Year
def print_by_year():
    for year in range(2008, 2023):
        #Create the first date for january 1
        year_start = "01/01/" + str(year)

        #Create the last day of the year
        month_day_data = monthrange(year, 12)
        last_day_in_month = month_day_data[1]

        year_end_day = str(last_day_in_month)
        year_end_month = "12"
        year_end_year = str(year)
        year_end = year_end_month + "/" + year_end_day + "/" + year_end_year
        
        print(year_start, " ", year_end)


print_by_year()


def print_by_month():
    print("need this ")
    
def print_by_day():
    print("need this ")







#MESSY NOTES BELOW

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

#if under 1000 write done to excel 
#else over 1000 write to excel not done 
#Point to file in status folder 
#data = status/aral.csv
#data = pd.read_csv('/Users/david/Desktop/David/www/geography/code/excelHandling/excel/updateExcel.csv', index_col=0)
#data = pd.read_csv('/Users/dvas22/Desktop/David/www/geography/examples/excelHandling/excel/updateExcel.csv', index_col=0)

'''
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
    #print(" ")'''


'''
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
'''