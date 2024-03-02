import math
import pandas as pd
import time


data = pd.read_csv('master_to_do/aral.csv', index_col=0)
#index	start_date	end_date	basin_count	finished
def main():
    for index, row in data.iterrows():
        start_date = row['start_date']
        end_date = row['end_date']
        basin_count = row['basin_count']
        finished = row['finished']
        print(index, start_date, end_date, basin_count, finished)

        if(math.isnan(index)):
            break
        
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
    data.loc[index, ['basin_count']] = [200] 
    writeStatus()
    time.sleep(1)


def writeStatus(): 
    print("The data was downloaded marking complete")
    df = pd.DataFrame(data)  
    df.to_csv('master_to_do/aral.csv')


if __name__ == "__main__":
    main()  
