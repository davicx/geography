import pandas as pd
import time


#data = pd.read_csv('/Users/david/Desktop/David/www/geography/code/excelHandling/excel/updateExcel.csv', index_col=0)
data = pd.read_csv('/Users/dvas22/Desktop/David/www/geography/examples/excelHandling/excel/updateExcel.csv', index_col=0)


def main():
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