import pandas as pd
import time


#data = pd.read_csv('/Users/david/Desktop/David/www/geography/code/excelHandling/excel/updateExcel.csv', index_col=0)
data = pd.read_csv('/Users/dvas22/Desktop/David/www/geography/status/year_loop.csv', index_col=0)


def main():
    for index, row in data.iterrows():
        basin = row['basin']
        start_date = row['start_date']
        end_date = row['end_date']
        basin_count = row['basin_count']
        over_one_thousand = row['over_one_thousand']
        finished = row['finished']
        print("Start Date ")
        print(start_date)
        print("End Date ")
        print(start_date)        
        if finished != 1:
            print("The data was downloaded marking complete")
            
            update_status(index)
            time.sleep(1)
        else:     
            print("The basin ", basin, " from ", start_date, " to ", end_date, " is already done so we are skipping")
            time.sleep(1)

def update_status(index):
    print("update_status")
    data.loc[index, ['finished']] = [1]
    df = pd.DataFrame(data)  
    df.to_csv('/Users/dvas22/Desktop/David/www/geography/status/year_loop.csv')

if __name__ == "__main__":
    main()  





