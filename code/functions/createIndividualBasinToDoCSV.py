import pandas as pd
import time


#Read Data in 
def main():
    data = pd.read_csv('data/MasterBasinToDo.csv', index_col=0)

    for index, row in data.iterrows():
        basin_code = row['basin_code']
        basin_count = int(row['basin_count'])
        print("New Basin ")
        print(basin_code, basin_count)
        createExcelToDo(basin_code, basin_count, 100)
        time.sleep(2)
        createPDFToDo(basin_code, basin_count, 1000)
        time.sleep(2)


#Download 1: Get full Excel
def createExcelToDo(basin_code, basin_count, max_downloads):
    index = []
    basin = ["hi"]
    start = []
    stop = []
    status = []

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
        status.append("n")

    current_object = {'index': index, 'basin_code': basin_code, 'min': start, 'max': stop, 'finished': status}
    df = pd.DataFrame(current_object)
    print(df)
    new_name = 'data/basins/excel/' + basin_code + '.csv'
    df.to_csv(new_name)

 
#Download 2: Get full PDFs
def createPDFToDo(basin_code, basin_count, max_downloads):
    index = []
    basin = ["hi"]
    start = []
    stop = []
    status = []

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
        status.append("n")

    current_object = {'index': index, 'basin_code': basin_code, 'min': start, 'max': stop, 'finished': status}
    df = pd.DataFrame(current_object)
    print(df)
    new_name = 'data/basins/pdf/' + basin_code + '.csv'
    df.to_csv(new_name)



if __name__ == "__main__":
    main()
