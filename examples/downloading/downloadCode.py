from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from chromedriver_py import binary_path  

import os
import sys
import pandas as pd
import time

''''


#STEP 3: Check Result and Group Duplicates
def check_excel_result_count(basin_code):
    print("FUNCTION A3: Check the Basin Count") 
    
    #Make sure that we group results
    basin_result_count_one = get_result_count()
    driver.find_element(By.CSS_SELECTOR, ".custom-control-indicator").click()
    time.sleep(5)
    basin_result_count_two = get_result_count()
    
    if basin_result_count_two > basin_result_count_one:
        driver.find_element(By.CSS_SELECTOR, ".custom-control-indicator").click()
        time.sleep(5)    

    print("Count 1- Current Page Count ", basin_result_count_two)
    print("Count 2- Current Page Count ", basin_result_count_two)
    basin_result_count_raw = min(basin_result_count_one, basin_result_count_two)
    basin_result_count = int(basin_result_count_raw)

    time.sleep(5)
    if basin_result_count == 0:
        print("nothing to download")
        
    elif basin_result_count > 0 and basin_result_count < 1000:
        print("We can just download") 
        download_excel(basin_code, basin_result_count)

    else: 
        print("Skip")

    #IF less then 1000 then download
    #If 0 Skip

    print("FUNCTION A3: Finished ")
    return basin_result_count

#STEP 4: Check Sort by Oldest to Newest 


#STEP 5: Download Excel (1000)
def download_excel(basin_code, basin_result_count):
    min = str(1)
    max = str(basin_result_count)

    print("STEP 5: Start Downloading Excel")

    print("Starting Downloads 1: Excel files for ", min, ": from ", 0, " to ", max)
    #/Users/david/Desktop/David/www/geography/downloads/excel/ARAL

    path = "/Users/david/Desktop/David/www/geography/downloads/excel/"

    download_start_stop = min + "-" + max
    download_file_name = "ResultsList_" + basin_code + "_202207_" + min + "_" + max

    driver.find_element(By.CSS_SELECTOR, ".has_tooltip:nth-child(1) > .la-Download").click()
    time.sleep(8)
    driver.find_element(By.ID, "ResultsListOnly").click()
    time.sleep(5)
    driver.find_element(By.ID, "XLSX").click()
    time.sleep(5)  

    #Send the total amount to download 
    driver.find_element(By.CSS_SELECTOR, ".nested:nth-child(3) #SelectedRange").click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, ".nested:nth-child(3) #SelectedRange").send_keys(download_start_stop)
    time.sleep(8)

    #Type in the Filename 
    driver.find_element(By.ID, "FileName").click()
    time.sleep(3)
    driver.find_element(By.ID, "FileName").send_keys("fileName")
    driver.find_element(By.ID, "FileName").clear()
    time.sleep(3)
    driver.find_element(By.ID, "FileName").send_keys(download_file_name)
    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, ".button-group > .primary").click()
    print("Finished downloads from ", min, " to ", max)
    time.sleep(20)

    #########
    #Everything worked to here just need to move the download this was new code
    
    #MOVE FILE: Set the File Name (Need to add in the dates for this)
    while download_wait < 10:
        try:
            #ResultsList_Aral_202207_1_60.ZIP
            print("File downloaded and moved to /Users/david/Desktop/David/www/geography/downloads/excel/", basin_code)

            original_path = "/Users/david/Desktop/David/www/geography/downloads/"
            fileNameOriginal = original_path + download_file_name + ".ZIP"

            final_path = "/Users/david/Desktop/David/www/geography/downloads/excel/"
            fileNameNew = final_path + basin_code + "/" + download_file_name + ".ZIP"

            os.rename(fileNameOriginal, fileNameNew)
            download_wait = 12
            time.sleep(5)

        except FileNotFoundError:
            print("The file has not finished downloading yet")
            download_wait = download_wait + 1
            time.sleep(5)

    
    download_wait = 0

    while download_wait < 10:
        try:
            #ResultsList_Aral_202207_1_60.ZIP
            print("File downloaded and moved to /Users/david/Desktop/David/www/geography/downloads/excel/", basin_code)
            fileNameOriginal = path + download_file_name + ".ZIP"
            fileNameNew = path + basin_code + "/" + download_file_name + ".ZIP"
            os.rename(fileNameOriginal, fileNameNew)

            time.sleep(5)
        except FileNotFoundError:
            print("The file has not finished downloading yet")
            download_wait = download_wait + 1
            time.sleep(5)
  

    print("STEP 3: Excel Downloads for ", basin_code, " FINISHED")
    time.sleep(1)

#STEP 3: Download Excel (1000)
def single_basin_excel_download(basin_code):
    print("Downloading Excel")
    singleBasinToDoFile = 'data/singleBasinToDo/adige/adige.csv'
    singleBasinToDo = pd.read_csv(singleBasinToDoFile)

    for index, row in singleBasinToDo.iterrows():
        start_date = row['start_date']
        end_date = row['end_date']
        finished = row['finished']

        if finished != 1:
            singleBasinToDo.loc[index, ['finished']] = [1] 
            print("DO! The dates ", start_date, end_date, " for basin ", basin_code, finished)
    
            #single_basin_search(basin_code, search_terms)
            
            #Mark Completed 
            df = pd.DataFrame(singleBasinToDo)  
            df.to_csv(singleBasinToDoFile)
  

            time.sleep(1)
        else:     
            print("The dates ", start_date, end_date, " for basin ", basin_code, " is already done so we are skipping ", finished)
            time.sleep(.2)
        #time.sleep(360)



#STEP 3: Download First Results of Excel Files
def download_results_one_excel(basin_code, basin_result_count):
    max_downloads = 100
    print("STEP 3: Starting to Download all excel Results for Basin Code ", basin_code) 
    paginate_downloads_one(basin_code, basin_result_count, max_downloads)
    print("STEP 3: Finished") 
    time.sleep(5)

#Step 3A: 
def paginate_downloads_one(basin_code, basin_result_count, max_downloads):
    basin_result_count = int(basin_result_count)

    for i in range(0, basin_result_count, max_downloads):
        min = i
        max = 0

        #Get Min
        if i != 0:
            min = min + 1
        else:
            min = 1

        #Get max
        if i + max_downloads > basin_result_count:
            max = basin_result_count
        else:
            max = i + max_downloads

        min_string = str(min)
        max_string = str(max)

        download_results_one(basin_code, min_string, max_string)
        #Move File
        time.sleep(5)


#Step 3B:       
def download_results_one(basin_code, min, max):
    print("Starting Downloads 1: Excel files for ", basin_code, ": from ", min, " to ", max)
    download_start_stop = min + "-" + max
    download_file_name = "ResultsList_" + basin_code + "_202207_" + min + "_" + max
    driver.find_element(By.CSS_SELECTOR, ".has_tooltip:nth-child(1) > .la-Download").click()
    time.sleep(8)
    driver.find_element(By.CSS_SELECTOR, ".DeliveryItemType > .row:nth-child(3) > label").click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, ".nested:nth-child(3) #SelectedRange").click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, ".nested:nth-child(3) #SelectedRange").send_keys(download_start_stop)
    time.sleep(4)
    driver.find_element(By.ID, "XLSX").click()
    time.sleep(5)
    driver.find_element(By.ID, "FileName").click()
    time.sleep(5)
    driver.find_element(By.ID, "FileName").send_keys("fileName")
    driver.find_element(By.ID, "FileName").clear()
    time.sleep(5)
    driver.find_element(By.ID, "FileName").send_keys(download_file_name)
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".button-group > .primary").click()
    print("Finished downloads from ", min, " to ", max)
    time.sleep(20)
    
    path = "/Users/david/Desktop/David/www/geography/downloads/"

    fileNameOriginal = path + download_file_name + ".ZIP"
    fileNameNew = path + basin_code + "/" + download_file_name + ".ZIP"
    os.rename(fileNameOriginal, fileNameNew)
    time.sleep(5)
    


#STEP 4: Download First Results of Excel Files (this can be slow)
def download_results_two_pdf(basin_code, basin_result_count):
    max_downloads = 100
    print("STEP 4: Starting to Download all pdf Results for Basin Code ", basin_code) 
    paginate_downloads_two(basin_code, basin_result_count, max_downloads)
    print("STEP 4: Finished") 
    time.sleep(5)

#Step 4A: 
def paginate_downloads_two(basin_code, basin_result_count, max_downloads):
    basin_result_count = int(basin_result_count)

    for i in range(0, basin_result_count, max_downloads):
        min = i
        max = 0

        #Get Min
        if i != 0:
            min = min + 1
        else:
            min = 1

        #Get max
        if i + max_downloads > basin_result_count:
            max = basin_result_count
        else:
            max = i + max_downloads

        min_string = str(min)
        max_string = str(max)

        download_results_two(basin_code, min_string, max_string)
        time.sleep(5)

#Step 4B: 
def download_results_two(basin_code, min, max):
    print("Starting Downloads 2: Get pdf files for ", basin_code, ": from ", min, " to ", max)
    download_start_stop = min + "-" + max
    #download_file_name = "ResultsList_adige_202207"
    download_file_name = "ResultsList2_" + basin_code + "_202207_" + min + "_" + max

    driver.find_element(By.CSS_SELECTOR, ".has_tooltip:nth-child(1) > .la-Download").click()
    time.sleep(5)

    driver.find_element(By.ID, "SelectedRange").click()
    driver.find_element(By.ID, "SelectedRange").send_keys(download_start_stop)
    time.sleep(2)
    
    driver.find_element(By.ID, "FileName").send_keys("fileName")
    driver.find_element(By.ID, "FileName").clear()
    time.sleep(2)

    driver.find_element(By.ID, "FileName").click()
    driver.find_element(By.ID, "FileName").send_keys(download_file_name)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".button-group > .primary").click()

    print("Pausing for download to finish")
    time.sleep(60)
    path = "/Users/david/Desktop/David/www/geography/downloads/"
    fileName = "Files (100).PDF"

    fileNameOriginal = path + fileName
    fileNameNew = path + basin_code + "/" + download_file_name + ".PDF"

    os.rename(fileNameOriginal, fileNameNew)


    time.sleep(5)


    #Function B1: Get Result Count 
def get_result_count():
    count_element = driver.find_element(By.CLASS_NAME, "countrendered")
    result_count = count_element.get_attribute('data-actualresultscount')

    return result_count

'''