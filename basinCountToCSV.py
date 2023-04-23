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
        data.loc[index, ['finished']] = ["True"]
        error = True

    if error == True:
        break 
    
    time.sleep(1)


df = pd.DataFrame(data)

print(df)
df.to_csv('data/basinToDo.csv')


    

#Update Data

#On Success rewrite current data

#NOTES
'''
basin = ["hi", "hi", "hello", "hello", "hello"]
start = ["1", "11","1", "11", "21"]
stop = ["10", "20","10", "20", "30"]
status = ["", "","", "", ""]

# dictionary of lists
shire = {'basin': basin, 'start': start, 'stop': stop, 'status': status}
     
df = pd.DataFrame(shire)
 
#print(df)
df.to_csv('data/basinToDo.csv')

updated_basin = []
updated_start = []
updated_stop = []
updated_status = []

for index, row in df.iterrows():
    basin = row['basin']
    start = row['start']
    stop = row['stop']

    #Create a new row
    updated_basin.append(basin)
    updated_start.append(start)
    updated_stop.append(stop)
    updated_status.append("done")

    print(basin)
    print(start, stop)
    print("")

    time.sleep(1)

# dictionary of lists
updated_basin = {'basin': updated_basin, 'start': updated_start, 'stop': updated_stop, 'status': updated_status}
     
df = pd.DataFrame(updated_basin)
 
#print(df)
df.to_csv('data/basinToDo.csv')
'''



'''
data = pd.read_csv('data/basinToDo.csv')

for index, row in data.iterrows():
    basin = row['basin']
    basin_count = row['basin_count']
    print(basin)
    print(basin_count)
    print("")

    time.sleep(1)
'''

