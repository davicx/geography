from classes.UserClass import UserClass
from classes.BasinClass import BasinClass

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
from selenium.common.exceptions import ElementNotInteractableException
from chromedriver_py import binary_path  

import os
import sys
import pandas as pd
import time

#USER INFORMATION: User and Basin Information Setup (sSet this for yourself and the current basin)
external_user = False
basin_code = "tigr" 
master_user = "selena"

#SETUP: 
#PART 1: Chrome Configuration 
options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")

#options.add_argument("user-data-dir=Users/<username>/Library/Application Support/Google/Chrome/Default")
#prefs = {'download.default_directory' : '/Users/dvas22/Desktop/David/www/geography/downloads'}
options.add_argument("user-data-dir=/tmp/storedLoginInformation4")
prefs = {'download.prompt_for_download' : False}
options.add_experimental_option('prefs', prefs)

service = Service()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#PART 2: File Paths for each user
currentUser = UserClass(basin_code, master_user, external_user)

currentUser.getName()
paths = currentUser.getPath("excel")


#Base Paths 
user_name = paths["user_name"]
geography_folder = paths["geography_folder"]
download_folder_temp = paths["download_folder_temp"]
download_folder = paths["download_folder"]
status_file = paths["status_file"]

#Search Terms
def get_search_term():
    try:
        # Load the Excel file into a Pandas DataFrame
        df = pd.read_excel('/path/to/TrackingSheet_basinterms.xlsx')

        # Find the row corresponding to the provided basin code
        row = df[df['BCODE'] == basin_code.upper()]
            
            # Check if the row exists
        if not row.empty:
            # Retrieve the search term from the DataFrame
            #return row['Basin_Specific_Terms'].values[0]
            search_term = row['Basin_Specific_Terms'].values[0]
            print(search_term)
        else:
            print(f"No search term found for basin code: {basin_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

#Set Basin Status CSV File 
status_data = pd.read_csv(status_file, index_col=0)


#Set Basin Status CSV File 
status_data = pd.read_csv(status_file, index_col=0)
#status_data = pd.read_csv(status_file, index_col=0, dtype ={'start_date': str, 'end_date':str})

def main():
    
    #OSU Login
    #single_login() #this is for non Tufts users 
    
    #Tufts Login:
    login_tufts_user(user_name)
    time.sleep(5)

    #Find the search terms in the tracking sheet
    #get_search_term()  
    
    #Run Main Program
    #single_basin_search() 
    time.sleep(60)

#### UTILITY FUNCTIONS ####   
#FUNCTIONS A: Login Related Functions (there are three login functions one for a Tufts user, one for an external user and one that will run once if the login session is not working)
#Function A1: Login an internal Tufts User 
def login_tufts_user(user_name):
    time.sleep(5)
    print("Logging in user with userName " + user_name)
    driver.get("https://login.ezproxy.library.tufts.edu/login?auth=tufts&url=http://www.nexisuni.com")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn-shib > .login").click()
    time.sleep(3)
    driver.find_element(By.ID, "username").send_keys(user_name)
    driver.find_element(By.ID, "password").send_keys("")

    #Wait for user to manually put in user name 60 seconds
    time.sleep(30)
    try:
        driver.find_element(By.NAME, "_eventId_proceed").click()
        time.sleep(10)
    except NoSuchElementException:  
        print("Logged In _eventId_proceed")

    try:
        driver.find_element(By.ID, "trust-browser-button").click()
        time.sleep(10)
    except NoSuchElementException:  
        print("Logged In trust-browser-button")
    time.sleep(20)

#Single Basin Search
def single_basin_search():
    print("MAIN: Starting a single basin search for ", basin_code)
    
    for index, row in status_data.iterrows():
        #basin = row['Basin_Name']
        basin = row['BCODE'] 
        start_date = row['start_date']
        end_date = row['end_date']
        finished = row['finished']

        if finished == 2:
             print(basin_code, " is done!")
             time.sleep(1)
             quit()

        if finished != 1:

            #STEP 1: Base Search 
            base_search()

            #STEP 2: Set Date Range
            change_date(basin_code, start_date, end_date)

            #STEP 3: Group Duplicates
            group_duplicates()

            #STEP 4: Set Sort by to Date (oldest to Newest)
            set_sort_by_date()

            #STEP 5: Get Current Result Count
            result_count = get_result_count()
            result_count_int = int(result_count)

            if result_count_int < 1000:

                #STEP 6: Download Excel 
                download_outcome = download_excel(basin_code, 1, result_count)

                #STEP 7: Mark complete
                if download_outcome == True:
                    file_min = "result_min_1" + "_"
                    file_max = "result_max_" + result_count + "_"
                    file_start_date = "start_date_" + start_date + "_"
                    file_end_date = "end_date_" + end_date
                    
                    final_file_name = "ResultsList_" + basin_code + "_202207_" + file_min + file_max + file_start_date + file_end_date

                    update_status_success(index, result_count, final_file_name)
                else: 
                    update_status_failure(index, result_count)

                print("MAIN: Finished the Basin")
                time.sleep(12)

            else: 
                update_status_over_limit(index, result_count)

        else:     
            print("The basin ", basin, " from ", start_date, " to ", end_date, " is already done so we are skipping")
            time.sleep(1)
    
#STEP 1: Navigate to advanced search
def base_search():
    driver.get('https://advance-lexis-com.ezproxy.library.tufts.edu/bisacademicresearchhome?crid=d00841b4-988c-4295-87f6-e917a5f787a2&pdmfid=1516831&pdisurlapi=true')
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".advanced-search").click() #click advanced search
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".menu-node:nth-child(2)").click() #click to search in News
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,102)")

    #Search terms, Box 1
    driver.find_element(By.CSS_SELECTOR, ".searchterm-input-box:nth-child(1)").send_keys('*water* OR river* OR lake OR dam OR stream OR tributary OR diversion OR irrigation OR pollution OR water quality OR flood! OR drought! OR channel OR canal OR hydroelect! OR reservoir OR groundwater OR aquifer OR drought OR recharge OR "water table" OR "bore hole"')
    #Box 1, "headlines and lead sections"
    driver.find_element(By.CSS_SELECTOR, ".search-input-row-outline > .dropdown:nth-child(3) > .icon").click() 
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".expanded .dropdown-option:nth-child(7) > .option-text").click()
    time.sleep(5)

    #Search terms, Box 2
    driver.find_element(By.CSS_SELECTOR, ".search-input-row:nth-child(2) .searchterm-input-box").send_keys('treaty OR agree! OR negotiat! OR resolution OR commission OR secretariat OR joint management OR basin management OR peace OR accord OR "peace accord" OR settle! OR cooperat! OR collaborat! OR disput! OR conflict! OR disagree! OR sanction! OR war OR troops OR "letter of protest" OR hostility OR "shots fired" OR boycott OR protest! OR appeal OR intent OR reject OR threat! OR force OR coerce OR assault OR fight OR demand OR disapprove OR diploma! OR statement OR memorandum')
    #Box 2, "headlines and lead sections"
    driver.find_element(By.CSS_SELECTOR, ".dropdown:nth-child(5) > .icon").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".expanded .dropdown-option:nth-child(7) > .option-description").click()
    time.sleep(5)

    #Box 3 search terms
    
    #driver.find_element(By.CSS_SELECTOR, ".searchterm-input-box:nth-child(3)").send_keys(search_term)
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".search-input-row:nth-child(3) .searchterm-input-box").send_keys(search_term)
    time.sleep(5)
    #Box 3, "headlines and lead sections"
    driver.find_element(By.CSS_SELECTOR, ".search-input-row:nth-child(3) .dropdown:nth-child(5) > .icon").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".expanded .dropdown-option:nth-child(7) > .option-description").click()
    time.sleep(5)

    #AND NOT, before box 4
    driver.find_element(By.CSS_SELECTOR, ".search-input-row:nth-child(4) .dropdown:nth-child(1) > .icon").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".expanded .dropdown-option:nth-child(5) > .option-description").click()
    time.sleep(5)
    #Search terms Box 4
    driver.find_element(By.CSS_SELECTOR, ".search-input-row:nth-child(4) .searchterm-input-box").send_keys('ocean OR navigat! OR nuclear OR "water cannon" OR "light water reactor" OR "mineral water" OR "hold water" OR "cold water" OR "hot water" OR "water canister" OR "water tight" OR " water down" OR "flood of refugees" OR Rivera OR Suez OR Panama OR oil OR drugs OR "three gorges" OR waterski OR watermelon OR dishwater OR waterproof OR "water resistant" OR "water bath" ')
    #Box 4, headlines and lead sections
    driver.find_element(By.CSS_SELECTOR, ".search-input-row:nth-child(4) .dropdown:nth-child(5) > .icon").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".expanded .dropdown-option:nth-child(7) > .option-description").click()
    time.sleep(5)

    #scroll down to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    #click search
    driver.find_element(By.CSS_SELECTOR, ".search").click()
    time.sleep(5)

#STEP 2: Set Date Range
def change_date(search_link, start_date, end_date):
    print("STEP 2: Set Date Range")
    print("Setting the date range from ", start_date, " to ", end_date)
    driver.execute_script("window.scrollTo(0,120)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,400)")
    time.sleep(2)

    #Step 1: Check if Min Val is Visibile (will be when the timeline button is clicked)
    attempt_to_open_timeline()

    set_min_date(search_link, start_date)
    set_max_date(search_link, end_date)

    driver.find_element(By.CSS_SELECTOR, ".save").click()
    time.sleep(4)
    print("STEP 2: Finished")

#Function 2A: Open the Timeline Button 
def attempt_to_open_timeline():
    print("Step 2A: Attempt to Open Timeline we will scroll to and try to click the button")
    timeline_opened = check_timeline_opened()

    #if the timeline is not opened then open it 
    if timeline_opened == False:
        #TO DO: Handle when this doesn't open
        open_timeline_button()


#Function 2B: Set Min date 
def set_min_date(search_link, start_date):
    print("Starting set_min_date")
    print(start_date)
    min_count = 0

    #Try to open the timeline window if it does not open get the page again to reset 
    while min_count < 5:
        try:
            min_val_button = driver.find_element(By.CSS_SELECTOR, ".min-val")   
            time.sleep(1)  
            min_count = 10 
        except NoSuchElementException:  
            print("NoSuchElementException couldn't find min value ", min_count)
            driver.get(search_link)
            time.sleep(4)

            attempt_to_open_timeline()
                    
            min_count = min_count + 1
        
    #Clear out the current date 
    for x in range(12):
        min_val_button.click()
        min_val_button.send_keys(Keys.BACKSPACE)
        time.sleep(.1)

    #Put the new date in
    min_val_button.send_keys(start_date)
    print("Min date set")
    time.sleep(2)

#Function 2C: Set Max date 
def set_max_date(search_link, end_date):
    print("Starting set_max_date ")
    print(end_date)
    max_count = 0

    try:
        driver.find_element(By.CSS_SELECTOR, ".max-val").click()
        time.sleep(1)   
    except NoSuchElementException:  
        print("NoSuchElementException couldn't find max value ", max_count)
        driver.get(search_link)
        time.sleep(4) 
        attempt_to_open_timeline()
        max_count = max_count + 1
        
 
    for x in range(12):
        driver.find_element(By.CSS_SELECTOR, ".max-val").send_keys(Keys.BACKSPACE)
        time.sleep(.2)   
    time.sleep(1)
 
    driver.find_element(By.CSS_SELECTOR, ".max-val").send_keys(end_date)
    print("Max date set")

    time.sleep(2)

#Function 2D: Open the Timeline Button
def open_timeline_button():
    timeline_opened = check_timeline_opened()
    #print("Check timeline status")
    #print(timeline_opened)

    if timeline_opened == False:
        print("The timeline is closed so we will open the timeline")

        #Open the Timeline
        try:
            driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()
            print("Found and opened the timeline")

            time.sleep(8)  
        except NoSuchElementException:  
            print("Couldn't find the timeline open button")

    else: 
        print("Timeline is opened")

    timeline_opened = check_timeline_opened()
    print("Final check on timeline ")
    print(timeline_opened)
    time.sleep(6)
    return timeline_opened

#Function 2E: Check if timeline open or closed 
def check_timeline_opened():
    timeline_opened = False

    try:
        min_val_temp = driver.find_element(By.CSS_SELECTOR, ".min-val")   
        timeline_opened = True
        #print("The timeline is opened")
    except NoSuchElementException:  
        timeline_opened = False
        #print("The timeline is not opened")
    return timeline_opened

#STEP 3: Get Result Count and Toggle the Group Duplicates to On (DONE) 
def group_duplicates():
    print("STEP 3: Group Duplicates- Get Result Count and Toggle the Group Duplicates to On ") 

    #We have to trigger this first due to a small glitch that prevents the basin count from showing up 
    driver.find_element(By.CSS_SELECTOR, ".custom-control-indicator").click()
    time.sleep(5)
    
    #Step 1: Get both of the results with the Group Duplicates Toggled on and off
    basin_result_count_one_raw = get_result_count()
    driver.find_element(By.CSS_SELECTOR, ".custom-control-indicator").click()
    time.sleep(5)
    basin_result_count_two_raw = get_result_count()

    if type(basin_result_count_one_raw) == None:
        print("ERROR: The basin count was not available so quit")
        quit() 
    
    #Convert Basin Count One to Int 
    basin_result_count_one = int(basin_result_count_one_raw)
    basin_result_count_two = int(basin_result_count_two_raw)
   
    #Step 2: Set Group duplicats to the lower of the two 
    if basin_result_count_two > basin_result_count_one:
        #print("basin_result_count_two was greater then basin_result_count_one so click the toggle again")
        driver.find_element(By.CSS_SELECTOR, ".custom-control-indicator").click()
        time.sleep(5)    
    else: 
        print("basin_result_count_one was greater then basin_result_count_two so do nothing")    

    basin_result_count = min(basin_result_count_one, basin_result_count_two)
    time.sleep(5)
    print("STEP 3: Finished")

    return basin_result_count


#STEP 4: Set Sort by to Date (oldest to Newest)
def set_sort_by_date(): 
    print("STEP 4: Set Sort by to Date (oldest to Newest)")

    try:
        driver.find_element(By.ID, "sortbymenulabel").click()
        time.sleep(3)
    except NoSuchElementException:  
        print("NoSuchElementException couldn't find sortbymenulabel")

    try:
        driver.find_element(By.CSS_SELECTOR, "#dropdownmenu > button:nth-child(5)").click()
        time.sleep(3)
    except NoSuchElementException:  
        print("NoSuchElementException couldn't click dropdownmenu")

    time.sleep(2)
    print("STEP 4: FINISHED")

#STEP 5: Get Current Result Count
def get_result_count():
    print("STEP 5: Get Current Result Count")
    result_count = -1
    try:
        count_element = driver.find_element(By.CLASS_NAME, "countrendered")
        result_count = count_element.get_attribute('data-actualresultscount')
        time.sleep(1)
    except NoSuchElementException:  
        print("ERROR: Could not get the result count no element")
    
    print("STEP 5: FINISHED")

    return result_count

#STEP 6: Download Excel  
def download_excel(basin_code, min_raw, max_raw):
    min = str(min_raw)
    max = str(max_raw)
    print("STEP 6: Download Excel Files") 
    print("Starting Downloads: Excel files for ", min, ": from ", 0, " to ", max)

    download_start_stop = min + "-" + max
    download_file_name = "ResultsList_" + basin_code + "_202207_" + min + "_" + max

    driver.find_element(By.CSS_SELECTOR, ".has_tooltip:nth-child(1) > .la-Download").click()
    time.sleep(6)
    driver.find_element(By.ID, "ResultsListOnly").click()
    time.sleep(4)
    driver.find_element(By.ID, "XLSX").click()
    time.sleep(4)  

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
    #print("Function C1: Finished downloads from ", min, " to ", max)
    
    download_outcome = move_rename_file(download_file_name, download_folder_temp, download_file_name, download_folder)

    time.sleep(6)
    print("download_outcome")
    print(download_outcome)
    print("download_outcome")
    print("STEP 7: FINISHED")

    return True

#Function 6A: Move and Rename a File
def move_rename_file(original_file_name, original_file_path, new_file_name, new_file_path):
    download_wait_count = 0
    total_wait_seconds = 0
    #/Users/dvas22/Downloads/ResultsList_Aral_202207_1_220.ZIP
    
    while download_wait_count < 20:
        try:
            original_file_full = original_file_path + original_file_name + ".ZIP"
            new_file_full = new_file_path + new_file_name + ".ZIP"

            print("Original Download Location")
            print(original_file_full)

            print("Moving file to Geography Download Folder Location")
            print(new_file_full)

            os.rename(original_file_full, new_file_full)
            print("Step 6: The file was sucesfully moved")
            download_wait_count = 20
            time.sleep(5)
            return True

        except FileNotFoundError:
            download_wait_count = download_wait_count + 1
            total_wait_seconds = total_wait_seconds + 1
            print("Step 6: The file has not finished downloading yet pausing to sleep")
            print("Step 6: Total Wait ", total_wait_seconds * 5)
            wait_seconds(5)
    
    #Return true if the files were downloaded and moved 
    if download_wait_count < 20:
        return True
    else:
        return False

#### UTILITY FUNCTIONS ####   
#FUNCTIONS A: Login Related Functions (there are three login functions one for a Tufts user, one for an external user and one that will run once if the login session is not working)
#Function A1: Login an internal Tufts User 
def login_tufts_user(user_name):
    time.sleep(3)
    print("Logging in user with userName " + user_name)
    driver.get("https://login.ezproxy.library.tufts.edu/login?auth=tufts&url=http://www.nexisuni.com")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn-shib > .login").click()
    time.sleep(3)
    driver.find_element(By.ID, "username").send_keys(user_name)
    driver.find_element(By.ID, "password").send_keys("")

    #Wait for user to manually put in user name 60 seconds
    time.sleep(30)
    try:
        driver.find_element(By.NAME, "_eventId_proceed").click()
        time.sleep(10)
    except NoSuchElementException:  
        print("Logged In _eventId_proceed")

    try:
        driver.find_element(By.ID, "trust-browser-button").click()
        time.sleep(10)
    except NoSuchElementException:  
        print("Logged In trust-browser-button")
    time.sleep(20)

