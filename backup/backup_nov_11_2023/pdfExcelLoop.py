import pandas as pd
import time


data = pd.read_csv('/Users/dvas22/Desktop/David/www/geography/status/pdf/aral.csv', index_col=0)
status_file = "/Users/dvas22/Desktop/David/www/geography/status/pdf/aral.csv"

def main():
    high_level_loop()

def high_level_loop(): 

    #MASTER: Master Loop over full Sheet 
    for index, row in data.iterrows():
        run_last_search = False
        basin = row['basin']
        key = row['key']
        start_date = row['start_date']
        end_date = row['end_date']
        finished = row['finished']
        set_date = row['set_date']
        start_count = row['start_count']
        stop_count = row['stop_count']
        basin_count = row['temp']
        #over_one_thousand = row['over_one_thousand']
        #file_name = row['file_name']
        finished = row['finished']

        #STEP 1: Set Date
        '''
        if set_date == 1:
            print("Set Date Function ", set_date)
        else:
            print("Good to go ", set_date)

        '''

        #STEP 2: Get Last row
        if basin_count > start_count and basin_count < stop_count:
            run_last_search = True

        #STEP 2: Run Search if it is not already Done
        if finished != 1:
            #print("Run for ", basin, " key ", key, " start_date", start_date, " end_date",  end_date, " start_count", start_count, " stop_count",  stop_count)
            
            if basin_count > stop_count or run_last_search == True:
                print("Run the search ", "start_count ", start_count, " stop_count ",  stop_count)
            
            else:
                print("We don't need but mark done ", stop_count)
                update_status_success(index, 200)
            
            #print("RUN LAST SEARCH ", run_last_search)
            
        else:     
            print("The basin ", basin, " from ", start_date, " to ", end_date, " is already done so we are skipping")

        time.sleep(1)
    print(" ")
    print(" ")   

def update_status_success(index, result_count):
    print("update_status_success")
    data.loc[index, ['finished']] = [1]
    #data.loc[index, ['basin_count']] = [result_count]
    df = pd.DataFrame(data)  
    df.to_csv(status_file)
    
if __name__ == "__main__":
    main()