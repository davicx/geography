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


#DRIVER
#Driver Type 1: 
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")

#options.add_argument("user-data-dir=Users/<username>/Library/Application Support/Google/Chrome/Default")
options.add_argument("user-data-dir=/tmp/david4")
prefs = {'download.default_directory' : '/Users/dvas22/Desktop/David/www/geography/downloads'}
prefs = {'download.prompt_for_download' : False}
options.add_experimental_option('prefs', prefs)

service = Service()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


#Driver Type 2: 
'''
driver = webdriver.Chrome(service=svc, options=options)

options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")

#options.add_argument("user-data-dir=/tmp/david")
options.add_argument("user-data-dir=/tmp/david2")
#download_directory = /Users/dvas22/Downloads 
#download_directory = /Users/dvas22/Desktop/David/www/geography/downloads
 
#prefs = {'download.default_directory' : '/Users/dvas22/Desktop/David/www/geography/downloads'}
#prefs = {'download.default_directory' : '/Users/david/Desktop/David/www/geography/downloads/temp'}
prefs = {'download.prompt_for_download' : False}
#prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
#chrome_options.add_experimental_option("prefs",{'download.prompt_for_download': True})
options.add_experimental_option('prefs', prefs)
#options.add_experimental_option("detach", True)
svc = webdriver.ChromeService(executable_path=binary_path)
'''

#USER: Set Tufts or External User 
external_user = True

#BASIN 
basin_code = "Aral"
search_terms = "Aral OR Syr Daria OR Naryn OR Amu Daria OR Syr Darya OR Amu Darya OR Akhangaran OR Chirchik"


#FILE PATHS
#Base Path
base_path_prefix = "/Users/dvas22/"
#base_path_prefix = "/Users/david/"

#Main 
base_path = base_path_prefix + "Desktop/David/www/geography/"

#Download Folder
download_folder_temp = base_path_prefix + "Downloads/"
download_folder = base_path + "downloads/aral/excel/"
download_folder_pdf = base_path + "downloads/aral/pdf/"

#Search Link
if external_user == True:
    search_link = "https://advance-lexis-com.ezproxy.library.tufts.edu/search/?pdmfid=1516831&crid=8346dc40-81b7-47ac-9469-cb518c95d880&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(*water*+OR+river*+OR+lake+OR+dam+OR+stream+OR+tributary+OR+diversion+OR+irrigation+OR+pollution+OR+water+quality+OR+flood!+OR+drought!+OR+channel+OR+canal+OR+hydroelect!+OR+reservoir+OR+groundwater+OR+aquifer+OR+drought+OR+recharge+OR+%22water+table%22+OR+%22bore+hole%22)+and+hlead(treaty+OR+agree!+OR+negotiat!+OR+resolution+OR+commission+OR+secretariat+OR+joint+management+OR+basin+management+OR+peace+OR+accord+OR+%22peace+accord%22+OR+settle!+OR+cooperat!+OR+collaborat!+OR+disput!+OR+conflict!+OR+disagree!+OR+sanction!+OR+war+OR+troops+OR+%22letter+of+protest%22+OR+hostility+OR+%22shots+fired%22+OR+boycott+OR+protest!+OR+appeal+OR+intent+OR+reject+OR+threat!+OR+force+OR+coerce+OR+assault+OR+fight+OR+demand+OR+disapprove+OR+diploma!+OR+statement+OR+memorandum)+and+hlead(Aral+OR+Syr+Daria+OR+Naryn+OR+Amu+Daria+OR+Syr+Darya+OR+Amu+Darya+OR+Akhangaran+OR+Chirchik)+and+not+hlead(ocean+OR+navigat!+OR+nuclear+OR+%22water+cannon%22+OR+%22light+water+reactor%22+OR+%22mineral+water%22+OR+%22hold+water%22+OR+%22cold+water%22+OR+%22hot+water%22+OR+%22water+canister%22+OR+%22water+tight%22+OR+%22+water+down%22+OR+%22flood+of+refugees%22+OR+Rivera+OR+Suez+OR+Panama+OR+oil+OR+drugs+OR+%22three+gorges%22+OR+waterski+OR+watermelon+OR+dishwater+OR+waterproof+OR+%22water+resistant%22+OR+%22water+bath%22)&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=undefined%7Calldates&pdfromadvancedsearchpage=true&ecomp=yxLg9kk&earg=pdpsf&prid=c0d34a78-a8aa-4c9b-8ad0-d00c56ca39bd"
else:
    search_link =  "https://advance-lexis-com.ezproxy.library.tufts.edu/search/?pdmfid=1516831&crid=928f5e0f-556b-4f46-bf5d-1c43de32c3f8&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(*water*+OR+river*+OR+lake+OR+dam+OR+stream+OR+tributary+OR+diversion+OR+irrigation+OR+pollution+OR+water+quality+OR+flood!+OR+drought!+OR+channel+OR+canal+OR+hydroelect!+OR+reservoir+OR+groundwater+OR+aquifer+OR+drought+OR+recharge+OR+%22water+table%22+OR+%22bore+hole%22)+and+hlead(treaty+OR+agree!+OR+negotiat!+OR+resolution+OR+commission+OR+secretariat+OR+joint+management+OR+basin+management+OR+peace+OR+accord+OR+%22peace+accord%22+OR+settle!+OR+cooperat!+OR+collaborat!+OR+disput!+OR+conflict!+OR+disagree!+OR+sanction!+OR+war+OR+troops+OR+%22letter+of+protest%22+OR+hostility+OR+%22shots+fired%22+OR+boycott+OR+protest!+OR+appeal+OR+intent+OR+reject+OR+threat!+OR+force+OR+coerce+OR+assault+OR+fight+OR+demand+OR+disapprove+OR+diploma!+OR+statement+OR+memorandum)+and+hlead(Aral+OR+Syr+Daria+OR+Naryn+OR+Amu+Daria+OR+Syr+Darya+OR+Amu+Darya+OR+Akhangaran+OR+Chirchik)+and+not+hlead(ocean+OR+navigat!+OR+nuclear+OR+%22water+cannon%22+OR+%22light+water+reactor%22+OR+%22mineral+water%22+OR+%22hold+water%22+OR+%22cold+water%22+OR+%22hot+water%22+OR+%22water+canister%22+OR+%22water+tight%22+OR+%22+water+down%22+OR+%22flood+of+refugees%22+OR+Rivera+OR+Suez+OR+Panama+OR+oil+OR+drugs+OR+%22three+gorges%22+OR+waterski+OR+watermelon+OR+dishwater+OR+waterproof+OR+%22water+resistant%22+OR+%22water+bath%22)&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=undefined%7Calldates&pdfromadvancedsearchpage=true&ecomp=yxLg9kk&earg=pdpsf&prid=0b27b868-b378-4485-8a1f-7dd4553471f9"


#BASIN STATUS
#/Users/dvas22/Desktop/David/www/geography/status/pdf 
status_data_date = pd.read_csv(base_path + 'status/pdf/aral_date.csv', index_col=0)

def main():
    single_login()
    #login_tufts_user()
    single_basin_search()
    time.sleep(360)


#Single Basin Search
def single_basin_search():
    print("MAIN: Starting a single basin search for ", basin_code)
    
    #For PDF this loops over aral_date.csv to get the date but then loops over the results in batches of 100 in aral.csv
    for index, row in status_data_date.iterrows():
        basin = row['basin']
        key = row['key']
        start_date = row['start_date']
        end_date = row['end_date']
        finished = row['finished']

        if finished != 1:

            #STEP 1: Base Search 
            base_search()

            #STEP 2: Group Duplicates
            #group_duplicates()

            #STEP 3: Set Date Range
            #use aral_date.csv
            change_date(search_link, start_date, end_date)

            #STEP 4: Set Sort by to Date (oldest to Newest)
            #set_sort_by_date()

            #STEP 5: Get Current Result Count
            result_count = get_result_count()
            result_count_int = int(result_count)

            if result_count_int < 1000:

                #STEP 7: Download PDF 
                download_outcome = download_pdf_bulk(index, basin_code, key, result_count)

                #Step 7A: Mark complete download needs to be for each batch of 100 this is 1000
                if download_outcome == True:
                    update_status_success(index, result_count)
                    print("Mark Done")
                else: 
                    update_status_failure(index, result_count)
                    print("Mark not done")

                print("FINISHED ONE DATE- Mark complete")
                time.sleep(12)
                #download_outcome = download_pdf(basin_code, 1, result_count)
                #download_outcome = download_bulk_pdf(basin_code, 1700)
                #download_outcome = download_excel(basin_code, 1, result_count)
                #use aral.csv
                #download_pdf(1, 100)
                

            else: 
                update_status_over_limit(index, result_count)
                print("Mark Over 1000")

        else:     
            print("The basin ", basin, " from ", start_date, " to ", end_date, " is already done so we are skipping")
            time.sleep(1)


#STEP 7: Download PDF
def download_pdf_bulk(index, basin_code, key, result_count_raw):
    print("LEVEL 1: download_pdf_bulk")
    #download_pdf(min_raw, max_raw)
    print("download_pdf(min_raw, max_raw)")
    print(index, key, basin_code, result_count_raw)
    time.sleep(360)
    print("STOP HERE THIS IS WHERE WE LOOP OVER THIS")

#loop over 1 to 100 out function true if all pdf for that year range worked
def download_pdf(key, min_raw, max_raw):
    print("LEVEL 2: download_pdf")
    min = str(min_raw)
    max = str(max_raw)
    print("Starting Downloads: PDF files for from ", min, " to ", max)
    download_start_stop = min + "-" + max
    download_file_name_temp = "temp"

    driver.find_element(By.CSS_SELECTOR, ".has_tooltip:nth-child(1) > .la-Download").click()
    time.sleep(5)

    driver.find_element(By.ID, "SelectedRange").click()
    driver.find_element(By.ID, "SelectedRange").send_keys(download_start_stop)
    time.sleep(2)
    
    driver.find_element(By.ID, "FileName").send_keys("fileName")
    driver.find_element(By.ID, "FileName").clear()
    time.sleep(2)

    driver.find_element(By.ID, "FileName").click()
    driver.find_element(By.ID, "FileName").send_keys(download_file_name_temp)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".button-group > .primary").click()

    print("Pausing for download to finish")
    original_file_name = "Files (100).PDF"
    download_file_name = "ResultsList_" + basin_code + "_202207_" + min + "_" + max + "_PDF"

    download_outcome = move_rename_file(original_file_name, download_folder_temp, download_file_name, download_folder_pdf)
    print("Download Outcome")
    print(download_outcome)
    print("STEP 7: FINISHED")

    return download_outcome


#STEP 1: Navigate to first level search
def base_search(): 
    print("STEP 1: Navigate to first level search")
    driver.get(search_link)
    print("STEP 1: Finished")
    time.sleep(4)

#STEP 2: Get Result Count and Toggle the Group Duplicates to On (DONE) 
def group_duplicates():
    print("STEP 2: Get Result Count and Toggle the Group Duplicates to On ") 

    #We have to trigger this first due to a small glitch that prevents the basin count from showing up 
    driver.find_element(By.CSS_SELECTOR, ".custom-control-indicator").click()
    time.sleep(5)
    
    #Step 1: Get both of the results with the Group Duplicates Toggled on and off
    basin_result_count_one_raw = get_result_count()
    driver.find_element(By.CSS_SELECTOR, ".custom-control-indicator").click()
    time.sleep(5)
    basin_result_count_two_raw = get_result_count()

    print("Types of basin counts")
    print(basin_result_count_one_raw)
    print(type(basin_result_count_one_raw))
    print(basin_result_count_two_raw)
    print(type(basin_result_count_two_raw))
    print("Types of basin counts")

    if type(basin_result_count_one_raw) == None:
        print("The basin count was not available so quit")
        quit() 
    
    #Convert Basin Count One to Int 
    basin_result_count_one = int(basin_result_count_one_raw)
    #basin_result_count_one_string = str(basin_result_count_one_raw)
    basin_result_count_two = int(basin_result_count_two_raw)
    #basin_result_count_two_string = str(basin_result_count_two_raw)
    
    #Step 2: Set Group duplicats to the lower of the two 
    if basin_result_count_two > basin_result_count_one:
        print("basin_result_count_two was greater then basin_result_count_one so click the toggle again")
        driver.find_element(By.CSS_SELECTOR, ".custom-control-indicator").click()
        time.sleep(5)    
    else: 
        print("basin_result_count_one was greater then basin_result_count_two so we are good")    

    basin_result_count = min(basin_result_count_one, basin_result_count_two)
    time.sleep(5)

    print("STEP 2: Finished ")

    return basin_result_count

#STEP 3: Set Date Range
def change_date(search_link, start_date, end_date):
    print("STEP 3: Set Date Range")
    print("DATE FROM ", start_date, " to ", end_date)
    driver.execute_script("window.scrollTo(0,120)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,400)")
    time.sleep(2)
    print("Scrolled Down")

    #Step 1: Check if Min Val is Visibile (will be when the timeline button is clicked)
    attempt_to_open_timeline()

    set_min_date(search_link, start_date)
    set_max_date(search_link, end_date)

    driver.find_element(By.CSS_SELECTOR, ".save").click()
    time.sleep(4)
    print("STEP 3: Finished")

#Function 3A: Set Min date 
def set_min_date(search_link, start_date):
    print("Starting set_min_date")
    print(start_date)
    min_count = 0

    #Try to open the timeline window if it does not open get the page again to reset 
    #selenium.common.exceptions.ElementNotInteractableException
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

#Function 3B: Set Max date 
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

#Function 3C: Open the Timeline Button
def open_timeline_button():
    timeline_opened = check_timeline_opened()
    print("Check timeline status")
    print(timeline_opened)

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

#Function 3D: Open the Timeline Button 
def attempt_to_open_timeline():
    print("Attempt to Open Timeline we will scroll to and try to click the button")
    timeline_opened = check_timeline_opened()
    print("timeline_opened status")
    print(timeline_opened)
    print("timeline_opened ")

    #if the timeline is not opened then open it 
    if timeline_opened == False:
        #TO DO: Handle when this doesn't open
        open_timeline_button()

#Function 3E: Check if timeline open or closed 
def check_timeline_opened():
    timeline_opened = False

    try:
        min_val_temp = driver.find_element(By.CSS_SELECTOR, ".min-val")   
        timeline_opened = True
        print("The timeline is opened")
    except NoSuchElementException:  
        timeline_opened = False
        print("The timeline is not opened")
    return timeline_opened

#STEP 5: Get Current Result Count
def get_result_count():
    result_count = -1
    try:
        count_element = driver.find_element(By.CLASS_NAME, "countrendered")
        result_count = count_element.get_attribute('data-actualresultscount')
        time.sleep(1)
    except NoSuchElementException:  
        print("Could not get the result count")

    return result_count

#STEP 6: Set Sort by to Date (oldest to Newest)
def set_sort_by_date(): 
    print("STEP 6: Set Sort by to Date (oldest to Newest)")
    print("STEP 6: FINISHED- needs to be done")


    



#Function 7A: Move and Rename a File
def move_rename_file(original_file_name, original_file_path, new_file_name, new_file_path):
    download_wait_count = 0
    total_wait_seconds = 0
    #/Users/dvas22/Downloads/ResultsList_Aral_202207_1_220.ZIP
    
    while download_wait_count < 40:
        try:
            original_file_full = original_file_path + original_file_name
            new_file_full = new_file_path + new_file_name + ".pdf"

            print("original_file_full")
            print(original_file_full)
            print("new_file_full")
            print(new_file_full)
            #print("ResultsList_Aral_202207_1_220")

            os.rename(original_file_full, new_file_full)
            print("The file was sucesfully moved")
            download_wait_count = 100
            time.sleep(5)
            return True

        except FileNotFoundError:
            download_wait_count = download_wait_count + 1
            total_wait_seconds = total_wait_seconds + 1
            print("The file has not finished downloading yet pausing to sleep")
            print("Total Wait ", total_wait_seconds * 5)
            wait_seconds(5)
    
    #Return true if the files were downloaded and moved 
    if download_wait_count < 40:
        return True
    else:
        return False


#### UTILITY FUNCTIONS ####   
#FUNCTIONS A: Login Related Functions (there are three login functions one for a Tufts user, one for an external user and one that will run once if the login session is not working)
#Function A1: Login an internal Tufts User 
def login_tufts_user():
    time.sleep(3)
    driver.get("https://login.ezproxy.library.tufts.edu/login?auth=tufts&url=http://www.nexisuni.com")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn-shib > .login").click()
    time.sleep(3)
    driver.find_element(By.ID, "username").send_keys("swalla05")
    driver.find_element(By.ID, "password").send_keys("")
    time.sleep(10)
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
    time.sleep(60)
    
#Function A2: Login an External User with Temporary Access
def login_external_user():
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


#FUNCTIONS C: Excel Functions 
#Function C1: Update as success
def update_status_success(index, result_count):
    print("update_status_success")
    status_data.loc[index, ['finished']] = [1]
    status_data.loc[index, ['basin_count']] = [result_count]
    df = pd.DataFrame(status_data)  
    df.to_csv('/Users/dvas22/Desktop/David/www/geography/status/amur.csv')
         
#Function C2: Update as Skipped
def update_status_failure(index, result_count):
    print("update_status_failure")
    status_data.loc[index, ['finished']] = [0]
    df = pd.DataFrame(status_data)  
    df.to_csv('/Users/dvas22/Desktop/David/www/geography/status/amur.csv')

#Function C3: Update as Over Limit
def update_status_over_limit(index, result_count):
    print("update_status_over_limit")
    status_data.loc[index, ['finished']] = [1]
    status_data.loc[index, ['over_one_thousand']] = [1]
    status_data.loc[index, ['basin_count']] = [result_count]
    df = pd.DataFrame(status_data)  
    df.to_csv('/Users/dvas22/Desktop/David/www/geography/status/amur.csv')


if __name__ == "__main__":
    main()





'''

    #STEP 2: Group Duplicates and Get Result Count 
    #basin_count = group_duplicates()
    #print("basin count ", basin_count)

    #STEP 3: Set Date Range
    data = pd.read_csv('/Users/dvas22/Desktop/David/www/geography/status/amur.csv', index_col=0)

    for index, row in data.iterrows():
        basin = row['basin']
        start_date = row['start_date']
        end_date = row['end_date']
        finished = row['finished']

        if finished != 1:
            print("The data was downloaded marking complete")
            #update_status(index)
            time.sleep(1)
        else:     
            print("The basin ", basin, " from ", start_date, " to ", end_date, " is already done so we are skipping")
            time.sleep(1)

        #LOOP through here 


    #30 June 2008 to 1 July 2023 
    #change_date(search_link, "01/01/2000", "02/01/2010")
    #print("Changed Date one!")
    #Have to refresh the page each time, yay!!
    #time.sleep(4)
    #driver.get(search_link)
    #time.sleep(4)
    #change_date(search_link, "02/01/2011", "03/01/2021")
    #print("we got here! ")

    #STEP 4: Set Sort by to Date (oldest to Newest) (SELENA)
    
    #STEP 5: Download Excel 
    basin_result_count = 800
    min = 1
    max = 500
    download_excel(basin_code, min, max)

'''