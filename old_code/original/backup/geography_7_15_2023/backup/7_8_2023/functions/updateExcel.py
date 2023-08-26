import pandas as pd
import time


data = pd.read_csv('data/updateExcel.csv', index_col=0)

def main():
    for index, row in data.iterrows():
        basin = row['basin']
        start = row['start']
        stop = row['stop']
        finished = row['finished']
        print(index, basin, start, stop, finished)
        
        if finished != 1:
            run_search(index)
            time.sleep(1)
        else:     
            print("The basin ", basin, " from ", start, " to ", stop, " is already done so we are skipping")
            time.sleep(1)
        print(" ")

def run_search(index):
    print("index ", index)
    #This will mark the column finished at the current index with 1 meaning it is done 
    data.loc[index, ['finished']] = [1] 
    writeStatus()


def writeStatus(): 
    print("The data was downloaded marking complete")
    df = pd.DataFrame(data)  
    df.to_csv('data/updateExcel.csv')


if __name__ == "__main__":
    main()  







'''
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