import pandas as pd
import time
from random import *


#data = pd.read_csv('/Users/david/Desktop/David/www/geography/code/excelHandling/excel/updateExcel.csv', index_col=0)
#data = pd.read_csv('/Users/dvas22/Desktop/David/www/geography/examples/excelHandling/excel/updateExcel.csv', index_col=0)
file_path = "/Users/david/Desktop/David/www/geography/status/amur.csv"
data = pd.read_csv(file_path, index_col=0)


def main():
    for index, row in data.iterrows():
        basin = row['basin']
        start_date = row['start_date']
        end_date = row['end_date']
        finished = row['finished']

        #The Basin is not done
        if finished != 1:
            total_records_found = randint(1, 1100)
            if total_records_found < 1000:
                print("The data was downloaded marking complete")
                update_status(index, total_records_found)
            else:
                print("The data was over 1000 so we will skip for now")
                update_status_over_limit(index, total_records_found)
            time.sleep(1)

        else:     
            print("The basin ", basin, " from ", start_date, " to ", end_date, " is already done so we are skipping")
            time.sleep(1)

#Success: The records were under 1000 and we finished this date range
def update_status(index, total_records_found):
    data.loc[index, ['finished']] = [1]
    data.loc[index, ['basin_count']] = [total_records_found]
    df = pd.DataFrame(data)  
    df.to_csv(file_path)

#The records were more then 1000 so we are skipping
def update_status_over_limit(index, total_records_found):
    data.loc[index, ['basin_count']] = [total_records_found]
    data.loc[index, ['over_one_thousand']] = [1]
    
    df = pd.DataFrame(data)  
    df.to_csv(file_path)


if __name__ == "__main__":
    main()  


'''
def run_search(index):
    data.loc[index, ['finished']] = [1] 
    writeStatus()

def writeStatus(): 
    print("The data was downloaded marking complete")
    df = pd.DataFrame(data)  
    #df.to_csv('/Users/david/Desktop/David/www/geography/code/excelHandling/excel/updateExcel.csv')
    df.to_csv('/Users/dvas22/Desktop/David/www/geography/examples/excelHandling/updateExcel.py')








error = False
error = True
    if error == True:
        break 

import pandas as pd
import time


#Read Data in 
data = pd.read_csv('data/basinToDo.csv', index_col=0)

for index, row in data.iterrows():
    error = False
    basin = row['basin']
    start = row['start']
    stop = row['stop']
    finished = row['finished']
    print(basin)
    print(start, stop)
    print(finished)
    print("")
    data.loc[index, ['finished']] = ["True"]
    
    if index == 2: 
        data.loc[index, ['finished']] = ["Location2"]
        error = True

    if error == True:
        break 
    
    time.sleep(1)


df = pd.DataFrame(data)

print(df)
df.to_csv('data/basinToDo.csv')
'''