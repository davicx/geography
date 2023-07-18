import os
import pandas as pd
import time


#MAIN:
def main():
    data = pd.read_csv('data/secondLevelSearch.csv')
    
    for index, row in data.iterrows():
        basin_count = 240
        max_downloads = 100
        basin_code = row['basin_code']
        print(basin_code)
        createToDo(basin_code, basin_count, max_downloads)
        time.sleep(60)

def createToDo(basin_code, basin_count, max_downloads):
    index = [0]
    basin = ["hi"]
    start = [1]
    stop = [2]

    for i in range(0, basin_count, max_downloads):
        min = i
        max = 0

        #Get Min
        if i != 0:
            min = min + 1
        else:
            min = 1

        #Get max
        if i + max_downloads > basin_count:
            max = basin_count
        else:
            max = i + max_downloads
            
        print(basin_code, min, max)
        index.append(i)
        basin.append(basin_code)
        start.append(min)
        stop.append(max)
        print(basin)
        print(start)
        print(stop)
        time.sleep(.5)
    
    current_object = {'index': index, 'basin_code': basin_code, 'min': min, 'max': max}
    df = pd.DataFrame(current_object)
    print(df)
    new_name = 'data/basins/' + basin_code + '.csv'
    df.to_csv(new_name)


    


'''
name = ["david", "frodo"]
location = ["shire", "Shire"]

# dictionary of lists
shire = {'name': name, 'location': location}
     
df = pd.DataFrame(shire)
 
print(df)
df.to_csv('names.csv')



name_dict = {
            'Name': ['a','b','c','d'],
            'Score': [90,80,95,20]
          }

df = pd.DataFrame(name_dict)
dt.to_csv('C:/Users/abc/Desktop/file_name.csv')
print (df)
'''


if __name__ == "__main__":
    main()