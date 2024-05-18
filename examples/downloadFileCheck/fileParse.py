import os
import pandas as pd
import time


data = pd.read_csv('/Users/david/Desktop/David/www/geography/examples/fileParse/aral.csv')

#Check Files
def check_files():
    #index	BCODE	Basin_Name	start_date	end_date	time_duration	basin_count	over_one_thousand	file_name	finished
    
    for index, row in data.iterrows():
        #index = row['index']
        file_name = row['file_name']
        expectedFile = file_name + ".ZIP"
        fileLocation = "/Users/david/Desktop/David/www/geography/examples/fileParse/"
        # /Users/david/Desktop/David/www/geography/examples/fileParse/index_0__basincode_aral__min_1_max_400__startdate_07_01_2023_enddate_03_15_2024.ZIP
        fileFound = os.path.isfile(fileLocation + expectedFile)

        if fileFound == True:
            print(file_name, " was found: ", fileFound)
            update_status_success(index)
        else:
            print(file_name, " was not found: ", fileFound)
            update_status_not_found(index)
        time.sleep(1)

def update_status_success(index):
    data.loc[index, ['finished']] = [1]
    df = pd.DataFrame(data)  
    df.to_csv('/Users/david/Desktop/David/www/geography/examples/fileParse/arals.csv')

def update_status_not_found(index):
    data.loc[index, ['finished']] = [0]
    df = pd.DataFrame(data)  
    df.to_csv('/Users/david/Desktop/David/www/geography/examples/fileParse/arals.csv')

    
check_files()

#EXAMPLE: index_0_basin_code_aral_min_1_max_400_start_date_07/01/2023_end_date_03/15/2024
#EXAMPLE: index_0__basincode_aral__min_1_max_400__startdate_07_01_2023_enddate_03_15_2024
#EXAMPLE: index_0__basincode_aral__min_1_max_400__startdate_07_01_2023_enddate_03_15_2024.ZIP

#STEPS:
'''
1) Loop over CSV
2) Get File Name from CSV
3) Confirm File exists
4) Check status if file name is empty or not there not present 
'''



fileName = "index_0__basincode_aral__min_1_max_400__startdate_07-01-2023__enddate_03-15-2024.ZIP"

def parse_file_name(fileName):
    fileArray = fileName.split("__")
    indexArray = fileArray[0].split("index_")
    index = indexArray[1]

    print(index)
    print(fileArray[1])
    print(fileArray[2])
    print(fileArray[3])
    print(fileArray[4])
    expectedFile = "index_0__basincode_aral__min_1_max_400__startdate_07_01_2023_enddate_03_15_2024.ZIP"
    fileLocation = "/Users/david/Desktop/David/www/geography/examples/fileParse/"
    # /Users/david/Desktop/David/www/geography/examples/fileParse/index_0__basincode_aral__min_1_max_400__startdate_07_01_2023_enddate_03_15_2024.ZIP
    fileFound = os.path.isfile(fileLocation + expectedFile)
    print(fileFound)


#parse_file_name(fileName)

'''
try:
    my_abs_path = my_file.resolve(strict=True)
except FileNotFoundError:
    # doesn't exist
else:
    # exists

    
IndexError
index_0__
basincode_aral__
min_1_max_400__
startdate_07-01-2023_enddate_03-15-2024
'''
