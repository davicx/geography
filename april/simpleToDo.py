import pandas as pd
import time

#Read Data in 
data = pd.read_csv('data/simpleToDo.csv', index_col=0)

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
            time.sleep(1)
        print("")


def run_search(index):
    print("index", index)
    data.loc[index, ['finished']] = [1] 
    writeStatus()


def writeStatus(): 
    df = pd.DataFrame(data)  
    df.to_csv('data/simpleToDo.csv')
    print(df)




if __name__ == "__main__":
    main()  

'''
error = False
error = True
    if error == True:
        break 
'''