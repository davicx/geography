import os
import pandas as pd
import time

#MAIN:
def main():
    run_downloads()

#MAIN: Run full Search 
def run_downloads():
    data = pd.read_csv('data/masterBasinToDo.csv')
    
    for index, row in data.iterrows():
        
        basin_code = row['basin_code']

        print("Creating folders for " + basin_code)
        create_download_folders(basin_code)
        time.sleep(1)

def create_download_folders(basin_code):
    newpath = '/Users/david/Desktop/David/www/geography/downloads/pdf/' +  basin_code
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    newpath = '/Users/david/Desktop/David/www/geography/downloads/excel/' +  basin_code
    if not os.path.exists(newpath):
        os.makedirs(newpath)

if __name__ == "__main__":
    main()