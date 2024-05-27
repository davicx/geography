from classes.UserClass import UserClass
from classes.BasinClass import BasinClass

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import ElementNotInteractableException
from chromedriver_py import binary_path  

import os
import sys
import pandas as pd
import time

#USER INFORMATION: User and Basin Information Setup (sSet this for yourself and the current basin)
external_user = True
basin_code = "aral" 
master_user = "david2"

#SETUP: 
#PART 1: Chrome Configuration 
options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")

#options.add_argument("user-data-dir=Users/<username>/Library/Application Support/Google/Chrome/Default")
#prefs = {'download.default_directory' : '/Users/dvas22/Desktop/David/www/geography/downloads'}
options.add_argument("user-data-dir=/tmp/storedLoginInformation3")
prefs = {'download.prompt_for_download' : False}
options.add_experimental_option('prefs', prefs)

service = Service()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#PART 2: File Paths for each user
currentUser = UserClass(basin_code, master_user, external_user)
currentBasin = BasinClass(basin_code, external_user)

currentUser.getName()
paths = currentUser.getPath("excel")

#Base Paths 
user_name = paths["user_name"]
geography_folder = paths["geography_folder"]
download_folder_temp = paths["download_folder_temp"]
download_folder = paths["download_folder"]
status_file = paths["status_file"]

#Search Link
search_link = currentBasin.get_basin_path()

#Set Basin Status CSV File 
status_data = pd.read_csv(status_file, index_col=0)

def main():
    
    #OSU Login
    single_login() #this is for non Tufts users 
    
    #Tufts Login:
    #login_tufts_user(user_name)
    
    #Run Main Program
    single_basin_search() 
    time.sleep(60)


#Single Basin Search
def single_basin_search():
    print("MAIN: Starting a single basin search for ", basin_code)
    
    for index, row in status_data.iterrows():
        #basin = row['Basin_Name']
        basin = row['BCODE'] 
        start_date = convert_date(row['start_date'])
        end_date = convert_date(row['end_date'])
        finished = row['finished']

        if finished == 2:
             print(basin_code, " is done!")
             time.sleep(1)
             quit()

        if finished != 1:

            #STEP 1: Base Search 
            base_search()

            #STEP 2: Set Date Range
            change_date(search_link, start_date, end_date)

            #STEP 3: Group Duplicates
            group_duplicates()

            #STEP 4: Set Sort by to Date (oldest to Newest)
            set_sort_by_date()

            #STEP 5: Get Current Result Count
            result_count = get_result_count()
            result_count_int = int(result_count)

            if result_count_int < 1000:

                #STEP 6: Download Excel 
                #Step 6A: Create the file name 
                #EXAMPLE: index_0__basincode_aral__min_1_max_400__startdate_07_01_2023_enddate_03_15_2024
                file_name_index = "index_" + index
                file_name_basin = "basin_code_" + basin_code
                file_name_min_max = "min_1_max_" + str(result_count)
                file_name_start_date = start_date.replace("/", "_")
                file_name_end_date = end_date.replace("/", "_")
                file_name_start_end_date = file_name_start_date + "_" + file_name_end_date

                download_file_name = file_name_index + "__" + file_name_basin + "__" + file_name_min_max + "__" + file_name_start_end_date 

                download_outcome = download_excel(download_file_name, 1, result_count)

                #STEP 7: Mark complete
                if download_outcome == True:
                    update_status_success(index, result_count, download_file_name)
                else: 
                    update_status_failure(index, result_count)

                print("MAIN: Finished the Basin")
                time.sleep(12)

            else: 
                update_status_over_limit(index, result_count)

        else:     
            print("The basin ", basin, " from ", start_date, " to ", end_date, " is already done so we are skipping")
            time.sleep(1)

#STEP 1: Navigate to first level search
def base_search(): 
    print("STEP 1: Navigate to first level search")

    try:
        driver.get(search_link)
    except Exception as e:
        print("ERROR: Step 1: Please check the search link and make sure that it is correct")
        print("search_link: ", search_link)
        sys.exit(1)
    
    print("STEP 1: Finished")
    time.sleep(4)

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
    print("Function 2A: Attempt to Open Timeline we will scroll to and try to click the button")
    timeline_opened = check_timeline_opened()

    #if the timeline is not opened then open it 
    if timeline_opened == False:
        #TO DO: Handle when this doesn't open
        open_timeline_button()


#Function 2B: Set Min date 
def set_min_date(search_link, start_date):
    print("Function 2B: Starting set_min_date")
    print(start_date)
    min_count = 0

    #Try to open the timeline window if it does not open get the page again to reset 
    while min_count < 5:
        try:
            min_val_button = driver.find_element(By.CSS_SELECTOR, ".min-val")   
            time.sleep(1)  
            min_count = 10 
        except NoSuchElementException:  
            print("Function 2B: NoSuchElementException couldn't find min value ", min_count)
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
    print("Function 2C: Starting to Set Timeline Max date")
    print(end_date)
    max_count = 0

    try:
        driver.find_element(By.CSS_SELECTOR, ".max-val").click()
        time.sleep(1)   
    except NoSuchElementException:  
        print("Function 2C: NoSuchElementException couldn't find max value ", max_count)
        driver.get(search_link)
        time.sleep(4) 
        attempt_to_open_timeline()
        max_count = max_count + 1
        
 
    for x in range(12):
        driver.find_element(By.CSS_SELECTOR, ".max-val").send_keys(Keys.BACKSPACE)
        time.sleep(.2)   
    time.sleep(1)
 
    driver.find_element(By.CSS_SELECTOR, ".max-val").send_keys(end_date)
    print("Function 2C: Finished Setting Timeline Max date")

    time.sleep(2)

#Function 2D: Open the Timeline Button
def open_timeline_button():
    print("Function 2D: Will try to open the timeline button")
    timeline_opened = check_timeline_opened()

    if timeline_opened == False:
        print("Function 2D: The timeline is closed so we will open the timeline")

        #Open the Timeline
        try:
            driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()
            print("Found and opened the timeline")

            time.sleep(8)  
        except NoSuchElementException:  
            print("Function 2D: Couldn't find the timeline open button")

    else: 
        print("Function 2D:Timeline is opened")

    timeline_opened = check_timeline_opened()
    print("Function 2D: Final check on timeline ")
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
        print("STEP 3: Error The basin count was not available so quit")
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
        print("STEP 4: NoSuchElementException couldn't find sortbymenulabel")

    try:
        driver.find_element(By.CSS_SELECTOR, "#dropdownmenu > button:nth-child(5)").click()
        time.sleep(3)
    except NoSuchElementException:  
        print("STEP 4: NoSuchElementException couldn't click dropdownmenu")

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
#def download_excel(basin_code, min_raw, max_raw):
def download_excel(download_file_name, min_raw, max_raw):
    min = str(min_raw)
    max = str(max_raw)
    print("STEP 6: Download Excel Files") 
    print("Starting Downloads: Excel files for ", min, ": from ", 0, " to ", max)

    download_start_stop = min + "-" + max

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
    
    download_outcome = move_rename_file(download_file_name, download_folder_temp, download_file_name, download_folder)

    time.sleep(6)
    print("STEP 6: Download Excel download_outcome")
    print(download_outcome)
    print("STEP 6: FINISHED")

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

            print("Function 6A: Original Download Location and Filename")
            print(original_file_full)

            print("Function 6A: New Download Location and Filename")
            print(new_file_full)

            os.rename(original_file_full, new_file_full)
            print("Function 6A: The file was sucesfully moved")
            download_wait_count = 20
            time.sleep(5)
            return True

        except FileNotFoundError:
            download_wait_count = download_wait_count + 1
            total_wait_seconds = total_wait_seconds + 1
            print("Function 6A: The file has not finished downloading yet pausing to sleep")
            print("Function 6A: Total Wait ", total_wait_seconds * 5)
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

    
#Function A2: Login an External User with Temporary Access
def login_external_user():
    print("LOGIN") 
    print("Step 1: Get base search link") 
    #driver.get("https://nam04.safelinks.protection.outlook.com/?url=https%3A%2F%2Ftufts.alma.exlibrisgroup.com%2Fview%2FemailLogin%3Finstitute%3D01TUN_INST%26jwt%3DeyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBbG1hIiwiYXVkIjoiUHJpbW8iLCJleHAiOjE2OTMwOTMzNzksImp0aSI6Ik9QSHBnNXFSbEZRWjVDUVhiUGFxM2ciLCJpYXQiOjE2OTMwODk3NzksIm5iZiI6MTY5MzA4OTY1OSwic3ViIjoicGF0cm9uIiwiaWQiOiIyMTE5MjU0ODI5MDAwMzg1MSIsIm5hbWUiOiJDaGFybGVzLCBEYXZpZCIsImVtYWlsIjoidmFzcXVlemRAb3JlZ29uc3RhdGUuZWR1IiwicHJvdmlkZXIiOiJFTUFJTCIsImZpcnN0X25hbWUiOiJEYXZpZCIsImxhc3RfbmFtZSI6IkNoYXJsZXMifQ.TGOloKdYD2xLHiedNJiHsM62Jrxc6fXLKqoxcMfrKuw%26backUrl%3Dhttps%253A%252F%252Ftufts.primo.exlibrisgroup.com%252Fprimaws%252FsuprimaLogin%253Fsortby%253Drank%2526vid%253D01TUN_INST%253A01TUN%2526lang%253Den%2526target-url%253Dhttps%25253A%25252F%25252Ftufts.primo.exlibrisgroup.com%25252Fdiscovery%25252Fsearch%25253Fsortby%25253Drank%252526vid%25253D01TUN_INST%25253A01TUN%252526lang%25253Den&data=05%7C01%7Cvasquezd%40oregonstate.edu%7C7567c95eff17406b9bd208dba685cd10%7Cce6d05e13c5e4d6287a84c4a2713c113%7C0%7C0%7C638286865856140715%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=%2BDGfY8G4tN8GpUeAlFW%2BZux%2BORKQxoVCePxKR9zqoUc%3D&reserved=0")
    time.sleep(2)
    driver.get("https://tufts.primo.exlibrisgroup.com/discovery/search?sortby=rank&vid=01TUN_INST:01TUN&lang=en")
    time.sleep(4)
    driver.find_element(By.ID, "searchBar").click()
    time.sleep(2)
    print("Step 2: Search for Nexis Uni") 
    driver.find_element(By.ID, "searchBar").send_keys("nexis uni")
    time.sleep(2)
    driver.find_element(By.ID, "searchBar").send_keys(Keys.ENTER)
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, "#alma991017244849703851availabilityLine0 > .availability-status").click()
    time.sleep(6)
    print("Step 3: Move to new window") 
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.CSS_SELECTOR, ".btn-library > .login").click()
    time.sleep(1)
    print("Step 4: Send Temporary Code") 
    driver.find_element(By.ID, "user").click()
    time.sleep(1)

    driver.find_element(By.ID, "user").send_keys("862295360")
    time.sleep(1)

    driver.find_element(By.NAME, "submit").click()
    print("Step 5: Finish pause to sleep")
    time.sleep(8)


#Function A3: Login that runs once (if the browser crashed you will have to login again)
def single_login():
    print("single login") 
    #driver.get("https://nam04.safelinks.protection.outlook.com/?url=https%3A%2F%2Ftufts.alma.exlibrisgroup.com%2Fview%2FemailLogin%3Finstitute%3D01TUN_INST%26jwt%3DeyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBbG1hIiwiYXVkIjoiUHJpbW8iLCJleHAiOjE2OTMwOTMzNzksImp0aSI6Ik9QSHBnNXFSbEZRWjVDUVhiUGFxM2ciLCJpYXQiOjE2OTMwODk3NzksIm5iZiI6MTY5MzA4OTY1OSwic3ViIjoicGF0cm9uIiwiaWQiOiIyMTE5MjU0ODI5MDAwMzg1MSIsIm5hbWUiOiJDaGFybGVzLCBEYXZpZCIsImVtYWlsIjoidmFzcXVlemRAb3JlZ29uc3RhdGUuZWR1IiwicHJvdmlkZXIiOiJFTUFJTCIsImZpcnN0X25hbWUiOiJEYXZpZCIsImxhc3RfbmFtZSI6IkNoYXJsZXMifQ.TGOloKdYD2xLHiedNJiHsM62Jrxc6fXLKqoxcMfrKuw%26backUrl%3Dhttps%253A%252F%252Ftufts.primo.exlibrisgroup.com%252Fprimaws%252FsuprimaLogin%253Fsortby%253Drank%2526vid%253D01TUN_INST%253A01TUN%2526lang%253Den%2526target-url%253Dhttps%25253A%25252F%25252Ftufts.primo.exlibrisgroup.com%25252Fdiscovery%25252Fsearch%25253Fsortby%25253Drank%252526vid%25253D01TUN_INST%25253A01TUN%252526lang%25253Den&data=05%7C01%7Cvasquezd%40oregonstate.edu%7C7567c95eff17406b9bd208dba685cd10%7Cce6d05e13c5e4d6287a84c4a2713c113%7C0%7C0%7C638286865856140715%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=%2BDGfY8G4tN8GpUeAlFW%2BZux%2BORKQxoVCePxKR9zqoUc%3D&reserved=0")
    time.sleep(2)
    driver.get("https://tufts.primo.exlibrisgroup.com/discovery/search?sortby=rank&vid=01TUN_INST:01TUN&lang=en")
    time.sleep(4)
    driver.find_element(By.ID, "searchBar").click()
    time.sleep(2)
    driver.find_element(By.ID, "searchBar").send_keys("nexis uni")
    time.sleep(2)
    driver.find_element(By.ID, "searchBar").send_keys(Keys.ENTER)
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, "#alma991017244849703851availabilityLine0 > .availability-status").click()
    time.sleep(6)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.CSS_SELECTOR, ".btn-library > .login").click()
    time.sleep(1)

    driver.find_element(By.ID, "user").click()
    time.sleep(1)

    driver.find_element(By.ID, "user").send_keys("862295360")
    time.sleep(1)

    driver.find_element(By.NAME, "submit").click()

    time.sleep(4)
 
#FUNCTIONS B: Utility Functions 
#Function B1: Wait for period of seconds with no messages
def wait_seconds(total_wait_seconds):
    countdown_seconds = range(total_wait_seconds, 1, -1)

    for time_left in countdown_seconds:
        time.sleep(1)

#Function B2: Wait for period of seconds with messages
def wait_seconds_message(total_wait_seconds):
    countdown_seconds = range(total_wait_seconds, 1, -1)

    for time_left in countdown_seconds:
        print(time_left , "seconds left in wait period") 
        time.sleep(1)
    print("1 second left in wait period")
    print("")


#Function B3: Convert excel date to correct format
def convert_date(date):
   """Convert date format to match this output (add leading zeros and make year 4 digits)
   Month/Day/Year
   01/01/2000
   """

    # Split date
   if "/" in date: 
        date_list = date.split('/')
        day = date_list[1]
        month = date_list[0]
        year = date_list[2]

   elif "-" in date:
        date_list = date.split('-')
        day = date_list[1]
        month = date_list[0]
        year = date_list[2]
   else: 
        day = "01"
        month = "01"
        year = "2000"
        print(date, "Date is not in correct format. Please check the status sheet ")
        sys.exit(1)

   if len(date_list) < 2:
        day = "01"
        month = "01"
        year = "2000"
        print(date, "Date is not in correct format. Please check the status sheet ")
        sys.exit(1)

   # Convert Day  
   if len(day) < 2:
        correct_day = "0" + day
   else:
        correct_day = day

   # Convert Month
   if len(month) < 2:
       correct_month = "0" + month
   else:
        correct_month = month

    # Convert Year
   if len(year) < 3:
        correct_year = "20" + year
   else:
        correct_year = year

   correct_date = correct_month + "/" + correct_day + "/" + correct_year

   return correct_date    
 

#FUNCTIONS C: Excel Functions 
#Function C1: Update as success
def update_status_success(index, result_count, file_name):
    print("update_status_success")
    status_data.loc[index, ['finished']] = [1]
    status_data.loc[index, ['basin_count']] = [result_count]
    status_data.loc[index, ['file_name']] = [file_name]
    df = pd.DataFrame(status_data)  
    df.to_csv(status_file)

#Function C2: Update as Skipped
def update_status_failure(index, result_count):
    print("update_status_failure")
    status_data.loc[index, ['finished']] = [0]
    df = pd.DataFrame(status_data)  
    df.to_csv(status_file)

#Function C3: Update as Over Limit
def update_status_over_limit(index, result_count):
    print("update_status_over_limit")
    status_data.loc[index, ['finished']] = [1]
    status_data.loc[index, ['over_one_thousand']] = [1]
    status_data.loc[index, ['basin_count']] = [result_count]
    df = pd.DataFrame(status_data)  
    df.to_csv(status_file)

if __name__ == "__main__":
    main()
