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

import os
import pandas as pd
import time

options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")
options.add_argument("user-data-dir=/tmp/david")
prefs = {'download.default_directory' : '/Users/david/Desktop/David/www/geography/downloads'}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

logged_in = True  


#MAIN:
def main():
    if logged_in == False:
        login()
    else: 
        #login_inside()
        basin_code = "Aral"
        search_terms = "Aral OR Syr Daria OR Naryn OR Amu Daria OR Syr Darya OR Amu Darya OR Akhangaran OR Chirchik"
        print("__________________________________________________________________________")
        print("START SINGLE BASIN SEARCH: Starting a search for the basin " + basin_code)
        print("__________________________________________________________________________")
        single_basin_search(basin_code, search_terms)

#SINGLE BASIN SEARCH
def single_basin_search(basin_code, search_terms):
    masterToDoFile = 'master_to_do/aral.csv'
    masterToDo = pd.read_csv(masterToDoFile)
    
    #Loop over every year from 2008 to 2022
    for index, row in masterToDo.iterrows():
        print("START: Single Year Search")
        search_link = row['link']
        start_date = row['start_date']
        end_date = row['end_date']
        finished = row['finished']

        if finished != 1:
            first_level_search(search_link)
            basin_result_count = -1
            basin_result_count = search_by_year(basin_code, search_terms, start_date, end_date)

            #Mark Completed
            masterToDo.loc[index, ['finished']] = [1] 
            masterToDo.loc[index, ['basin_count']] = [basin_result_count] 

            if basin_result_count > 1000:
                masterToDo.loc[index, ['over_thousand']] = [1] 

            df = pd.DataFrame(masterToDo)  
            df.to_csv(masterToDoFile)
            print("Finished a single year from ", start_date, " to ", end_date, " and marking completed") 

            time.sleep(30)

        else:     
            print("The basin ", basin_code, " is already done so we are skipping")
            time.sleep(.5)

        print("END: Single Year Search ")  
        print("_____________________________________")  
        print(" ")  

#SINGLE SEARCH: Navigate through everything for a given year 
def search_by_year(basin_code, search_terms, start_date, end_date):

    #Step 2: Navigate to the second search terms that are basin specific 
    second_level_search(search_terms)

    #Step 3: Get the basin count and write to excel 
    basin_result_count = check_excel_result_count(basin_code, start_date, end_date)

    #Step 5: Download all excel results    
    if basin_result_count == 0:
        print("nothing to download")
        
    elif basin_result_count > 0 and basin_result_count < 1000:
        download_excel(basin_code, basin_result_count, start_date, end_date)

    else: 
        print("Skip")

    return basin_result_count


#STEP 1: Navigate to First Level Search
def first_level_search(search_link):	
    print("STEP 1: Starting First Level Search") 
    landing_page = 'https://advance-lexis-com.oregonstate.idm.oclc.org/bisacademicresearchhome/?pdmfid=1516831&crid=0f1105ae-7bcf-49e0-b0bd-1f5d6657e6ec&ecomp=zxryk&prid=86dd402e-b3c1-43d7-a5b0-308dbc0270c9'
    driver.get(landing_page)
    time.sleep(4)
    driver.get(search_link)
    time.sleep(4)
    print("STEP 1: Finished First Level Search") 
    print(" ")


#STEP 2: Navigate to Second Level Search 
def second_level_search(search_terms):	
    print("STEP 2: Starting Second Level Search") 
    driver.execute_script("window.scrollTo(0,103)")
    time.sleep(8)

    driver.find_element(By.CSS_SELECTOR, ".excludeContainer input").click()
    driver.find_element(By.NAME, "includeExcludeSearchTerm").click()
    driver.find_element(By.ID, "kmnyk_search").click()
    driver.find_element(By.ID, "kmnyk_search").send_keys(search_terms)
    driver.find_element(By.CSS_SELECTOR, ".src-submit").click()
    
    time.sleep(5)
    print("STEP 2: Finished Second Level Search") 
    print(" ")

#DOWNLOAD: EXCEL 
#STEP 3: Check Result and Group Duplicates
def check_excel_result_count(basin_code, start_date, end_date):
    print("STEP 3: Check Result and Group Duplicates")
    
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

    print("STEP 3: Finished")
    print(" ")
    return basin_result_count

#STEP 4: Check Sort by Oldest to Newest 


#STEP 5: Download Excel (1000)
def download_excel(basin_code, basin_result_count, start_date, end_date):
    print("STEP 5: Start Downloading Excel")
    min = str(1)
    max = str(basin_result_count)

    print("Step 5A: Starting Downloads for Excel files for ", min, ": from ", 0, " to ", max)

    download_start_stop = min + "-" + max
    start_date_array = start_date.split('/')
    end_date_array = end_date.split('/')
    start_year = start_date_array[2]
    end_year = end_date_array[2]

    download_file_name = "ResultsList_" + basin_code + "_202207_" + start_year + "_" + end_year

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
    time.sleep(20)
 
    #MOVE FILE: Set the File Name (Need to add in the dates for this)
    download_wait = 0
    print("Step 5B: Finished downloads from ", min, " to ", max)

    while download_wait < 20:
        try:
            print("Step 5C: File downloaded and trying to move")

            original_path = "/Users/david/Desktop/David/www/geography/downloads/"
            fileNameOriginal = original_path + download_file_name + ".ZIP"

            final_path = "/Users/david/Desktop/David/www/geography/downloads/excel/"
            fileNameNew = final_path + basin_code + "/" + download_file_name + ".ZIP"

            os.rename(fileNameOriginal, fileNameNew)

            print("Step 5D: File downloaded and moved from ")
            print(fileNameOriginal)
            print("to")
            print(fileNameNew)
            download_wait = 40
            time.sleep(5)

        except FileNotFoundError:
            print("Step 5 (Pending): The file has not finished downloading yet")
            download_wait = download_wait + 1
            time.sleep(5)

    print("STEP 5: Excel Downloads for ", basin_code, " FINISHED")
    print(" ")
    time.sleep(1)

#STEP 6: Download PDF (250)


#STEP 1: Navigate to Single Search (Includes Dates)
#STEP 2: Navigate to Second Level Search 
#STEP 3: Check Group Duplicates
#STEP 4: Check Sort by Oldest to Newest 
#STEP 5: Download Excel (1000)
    #Step 5A: Get Result Count (for the specific basin and time frame)
    #Step 5B: Paginate the Results
    #Step 5C: Download These to the correct folder
#STEP 6: Download PDF (250)
    #Step 6A: Get Result Count (for the specific basin and time frame)
    #Step 6B: Paginate the Results
    #Step 6C: Download These to the correct folder






#FUNCTIONS
#Function 1: Login a User
def login():
    print("Login") 
    driver.get("https://library.oregonstate.edu/")
    time.sleep(3)

    element = driver.find_element(By.ID,"term-1search")
    element.send_keys("nexis uni")
    element.send_keys(Keys.RETURN)
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, "#SEARCH_RESULT_RECORDID_alma99492178701865 mark").click()
    time.sleep(6)
    driver.find_element(By.CSS_SELECTOR, ".item-title:nth-child(1)").click()
    time.sleep(12)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(720)
    driver.find_element(By.CSS_SELECTOR, ".advanced-search").click()
    print("login: was run you can now start the search")
    time.sleep(720)

#Function 1: Login a User
def login_inside():
    print("Login") 
    driver.get("https://library.oregonstate.edu/")
    time.sleep(3)

    element = driver.find_element(By.ID,"term-1search")
    element.send_keys("nexis uni")
    element.send_keys(Keys.RETURN)
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, "#SEARCH_RESULT_RECORDID_alma99492178701865 mark").click()
    time.sleep(6)
    driver.find_element(By.CSS_SELECTOR, ".item-title:nth-child(1)").click()
    time.sleep(12)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(20)
    #driver.find_element(By.CSS_SELECTOR, ".advanced-search").click()
    print("login: was run you can now start the search")
  
def get_result_count():
    result_count_raw = driver.find_element(By.CSS_SELECTOR, ".countrendered")
    result_count = result_count_raw.text

    time.sleep(6)
    
    return result_count

if __name__ == "__main__":
    main()






   