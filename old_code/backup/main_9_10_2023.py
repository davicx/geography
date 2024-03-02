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

options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")
options.add_argument("user-data-dir=/tmp/david")
#options.add_argument("user-data-dir=/tmp/david2")
prefs = {'download.default_directory' : '/Users/dvas22/Desktop/David/www/geography/downloads'}
options.add_experimental_option('prefs', prefs)
#options.add_experimental_option("detach", True)

#Driver Type 1: The two driver types are dependent on which computer setup this is running on
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#Driver Type 2: 
svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc, options=options)

#Set Tufts or External User 
external_user = True

#Set login status 
logged_in = False  

def main():
    if logged_in == False:
        if external_user == True:
            login_external_user()
        else:
            login_tufts_user()
        
        time.sleep(60)
    else: 
        driver.get("https://www.google.com/")
        single_login()
        single_basin_search()
        time.sleep(60)


def single_basin_search():
    basin_code = "Aral"
    search_terms = "Aral OR Syr Daria OR Naryn OR Amu Daria OR Syr Darya OR Amu Darya OR Akhangaran OR Chirchik"
    print("Starting a single basin search for ", basin_code)
    time.sleep(1)

    #STEP 1: Get Base Search
    if external_user == True:
        search_link = "https://advance-lexis-com.ezproxy.library.tufts.edu/search/?pdmfid=1516831&crid=8346dc40-81b7-47ac-9469-cb518c95d880&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(*water*+OR+river*+OR+lake+OR+dam+OR+stream+OR+tributary+OR+diversion+OR+irrigation+OR+pollution+OR+water+quality+OR+flood!+OR+drought!+OR+channel+OR+canal+OR+hydroelect!+OR+reservoir+OR+groundwater+OR+aquifer+OR+drought+OR+recharge+OR+%22water+table%22+OR+%22bore+hole%22)+and+hlead(treaty+OR+agree!+OR+negotiat!+OR+resolution+OR+commission+OR+secretariat+OR+joint+management+OR+basin+management+OR+peace+OR+accord+OR+%22peace+accord%22+OR+settle!+OR+cooperat!+OR+collaborat!+OR+disput!+OR+conflict!+OR+disagree!+OR+sanction!+OR+war+OR+troops+OR+%22letter+of+protest%22+OR+hostility+OR+%22shots+fired%22+OR+boycott+OR+protest!+OR+appeal+OR+intent+OR+reject+OR+threat!+OR+force+OR+coerce+OR+assault+OR+fight+OR+demand+OR+disapprove+OR+diploma!+OR+statement+OR+memorandum)+and+hlead(Aral+OR+Syr+Daria+OR+Naryn+OR+Amu+Daria+OR+Syr+Darya+OR+Amu+Darya+OR+Akhangaran+OR+Chirchik)+and+not+hlead(ocean+OR+navigat!+OR+nuclear+OR+%22water+cannon%22+OR+%22light+water+reactor%22+OR+%22mineral+water%22+OR+%22hold+water%22+OR+%22cold+water%22+OR+%22hot+water%22+OR+%22water+canister%22+OR+%22water+tight%22+OR+%22+water+down%22+OR+%22flood+of+refugees%22+OR+Rivera+OR+Suez+OR+Panama+OR+oil+OR+drugs+OR+%22three+gorges%22+OR+waterski+OR+watermelon+OR+dishwater+OR+waterproof+OR+%22water+resistant%22+OR+%22water+bath%22)&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=undefined%7Calldates&pdfromadvancedsearchpage=true&ecomp=yxLg9kk&earg=pdpsf&prid=c0d34a78-a8aa-4c9b-8ad0-d00c56ca39bd"
    else:
        search_link =  "https://advance-lexis-com.ezproxy.library.tufts.edu/search/?pdmfid=1516831&crid=928f5e0f-556b-4f46-bf5d-1c43de32c3f8&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(*water*+OR+river*+OR+lake+OR+dam+OR+stream+OR+tributary+OR+diversion+OR+irrigation+OR+pollution+OR+water+quality+OR+flood!+OR+drought!+OR+channel+OR+canal+OR+hydroelect!+OR+reservoir+OR+groundwater+OR+aquifer+OR+drought+OR+recharge+OR+%22water+table%22+OR+%22bore+hole%22)+and+hlead(treaty+OR+agree!+OR+negotiat!+OR+resolution+OR+commission+OR+secretariat+OR+joint+management+OR+basin+management+OR+peace+OR+accord+OR+%22peace+accord%22+OR+settle!+OR+cooperat!+OR+collaborat!+OR+disput!+OR+conflict!+OR+disagree!+OR+sanction!+OR+war+OR+troops+OR+%22letter+of+protest%22+OR+hostility+OR+%22shots+fired%22+OR+boycott+OR+protest!+OR+appeal+OR+intent+OR+reject+OR+threat!+OR+force+OR+coerce+OR+assault+OR+fight+OR+demand+OR+disapprove+OR+diploma!+OR+statement+OR+memorandum)+and+hlead(Aral+OR+Syr+Daria+OR+Naryn+OR+Amu+Daria+OR+Syr+Darya+OR+Amu+Darya+OR+Akhangaran+OR+Chirchik)+and+not+hlead(ocean+OR+navigat!+OR+nuclear+OR+%22water+cannon%22+OR+%22light+water+reactor%22+OR+%22mineral+water%22+OR+%22hold+water%22+OR+%22cold+water%22+OR+%22hot+water%22+OR+%22water+canister%22+OR+%22water+tight%22+OR+%22+water+down%22+OR+%22flood+of+refugees%22+OR+Rivera+OR+Suez+OR+Panama+OR+oil+OR+drugs+OR+%22three+gorges%22+OR+waterski+OR+watermelon+OR+dishwater+OR+waterproof+OR+%22water+resistant%22+OR+%22water+bath%22)&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=undefined%7Calldates&pdfromadvancedsearchpage=true&ecomp=yxLg9kk&earg=pdpsf&prid=0b27b868-b378-4485-8a1f-7dd4553471f9"
    
    driver.get(search_link)
    time.sleep(4)

    #STEP 2: Group Duplicates and Get Result Count 
    basin_count = group_duplicates()
    print("basin count ", basin_count)

    #STEP 3: Set Date Range 
    #change_date(search_link, "01/01/2000", "02/01/2010")
    #change_date(search_link, "02/01/2010", "03/01/2020")
    #print("we got here! ")

    #STEP 3: Set Sort by to Date (oldest to Newest)

    #STEP 4: Download Excel  
    download_excel(basin_code, basin_result_count)

    #STEP 5: Download PDF 


   
#FUNCTIONS B: Utility Functions 
#Function B1: Get Result Count 
def get_result_count():
    count_element = driver.find_element(By.CLASS_NAME, "countrendered")
    result_count = count_element.get_attribute('data-actualresultscount')

    return result_count

#Function B2: Get Result Count and Toggle the Group Duplicates to On 
def group_duplicates():
    print("STEP 1: Get Result Count and Toggle the Group Duplicates to On ") 

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

    print("STEP 1: Finished ")

    return basin_result_count


#Function B3: Set Date Range 
def change_date(search_link, start_date, end_date):
    print("STEP 3: Set Sort by to Date (oldest to Newest)")
    driver.execute_script("window.scrollTo(0,120)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,400)")
    time.sleep(2)
    print("Scrolled Down")

    #Step 1: Open the timeline 
    #May need to open and close if timeline selector value does not show up sometimes it loads slow or does not load
    driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()

    time.sleep(4)

    start_date = "01/01/1980"
    set_min_date(search_link, start_date)
    set_max_date(search_link, end_date)

    driver.find_element(By.CSS_SELECTOR, ".save").click()
    time.sleep(4)

    #NOTES
    '''
    #This seems to work
    driver.execute_script("window.scrollTo(0,10)")
    driver.execute_script("window.scrollTo(0,400)")
    driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()
    driver.find_element(By.CSS_SELECTOR, ".min-val").click()
    driver.find_element(By.CSS_SELECTOR, ".min-val").send_keys("open")
    driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()
    driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()
    driver.find_element(By.CSS_SELECTOR, ".min-val").click()
    driver.find_element(By.CSS_SELECTOR, ".min-val").send_keys("open")
    '''

#Function B4: Set Minimum Date Value
def set_min_date(search_link, start_date):
    min_count = 0

    #Try to open the timeline window if it does not open get the page again to reset 
    #selenium.common.exceptions.ElementNotInteractableException
    while min_count < 5:
        try:
            driver.find_element(By.CSS_SELECTOR, ".min-val").click()
            time.sleep(1)  
            min_count = 10 
        except NoSuchElementException:  
            print("NoSuchElementException couldn't find min value ", min_count)
            driver.get(search_link)
            time.sleep(4) 
            min_count = min_count + 1
    
    #Clear out the current minimum date
    for x in range(12):
        driver.find_element(By.CSS_SELECTOR, ".min-val").send_keys(Keys.BACKSPACE)
        time.sleep(.2)
    time.sleep(1)

    #Put the new date in
    driver.find_element(By.CSS_SELECTOR, ".min-val").send_keys(start_date)
    time.sleep(2)
    #If fails return false 

#Function B5: Set Maximum Date Value
def set_max_date(search_link, end_date):
    max_count = 0

    try:
        driver.find_element(By.CSS_SELECTOR, ".max-val").click()
        time.sleep(1)   
    except NoSuchElementException:  
        print("NoSuchElementException couldn't find min value ", max_count)
        driver.get(search_link)
        time.sleep(4) 
        max_count = max_count + 1
        #driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()

    for x in range(12):
        driver.find_element(By.CSS_SELECTOR, ".max-val").send_keys(Keys.BACKSPACE)
        time.sleep(.2)   
    time.sleep(1)
 
    driver.find_element(By.CSS_SELECTOR, ".max-val").send_keys(end_date)
    time.sleep(2)
    

#FUNCTIONS C: Download Excel Files 
#Function C1: Download Excel File 
def download_excel(basin_code, basin_result_count):
    min = str(1)
    max = str(basin_result_count)

    print("Function C1: Download Excel File")
    print("Starting Downloads 1: Excel files for ", min, ": from ", 0, " to ", max)

    download_start_stop = min + "-" + max
    #download_file_name = "ResultsList_" + basin_code + "_202207_" + min + "_" + max
    download_file_name = "aral"

    driver.find_element(By.CSS_SELECTOR, ".has_tooltip:nth-child(1) > .la-Download").click()
    time.sleep(4)
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
    print("Function C1: Finished downloads from ", min, " to ", max)
    time.sleep(60)

#Function C2: Move and Rename Excel File 


#FUNCTIONS D: Download PDF Files  




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
 
if __name__ == "__main__":
    main()





#APPENDIX: Code and Notes
'''
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


#MAIN 
        basin_code = "Aral"
        search_terms = "Aral OR Syr Daria OR Naryn OR Amu Daria OR Syr Darya OR Amu Darya OR Akhangaran OR Chirchik"
        print("START SINGLE BASIN SEARCH: Starting a search for the basin " + basin_code)
        single_basin_search(basin_code, search_terms)


def single_basin_search(basin_code, search_terms):
    first_level_search(basin_code, search_terms)


#STEP 1: Navigate to Single Search (Includes Dates)
def first_level_search(basin_code, search_terms): 
    print("#STEP 1: Navigate to Single Search")
    landing_page = 'https://advance-lexis-com.oregonstate.idm.oclc.org/bisacademicresearchhome/?pdmfid=1516831&crid=0f1105ae-7bcf-49e0-b0bd-1f5d6657e6ec&ecomp=zxryk&prid=86dd402e-b3c1-43d7-a5b0-308dbc0270c9'
    
    first_level_page_part_one = 'https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=b1785a07-3220-42ca-b9e0-cfa91bb98ae1&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(*water*+OR+river*+OR+lake+OR+dam+OR+stream+OR+tributary+OR+diversion+OR+irrigation+OR+pollution+OR+water+quality+OR+flood!+OR+drought!+OR+channel+OR+canal+OR+hydroelect!+OR+reservoir+OR+groundwater+OR+aquifer+OR+drought+OR+recharge+OR+%22water+table%22+OR+%22bore+hole%22)+and+hlead(treaty+OR+agree!+OR+negotiat!+OR+resolution+OR+commission+OR+secretariat+OR+joint+management+OR+basin+management+OR+peace+OR+accord+OR+%22peace+accord%22+OR+settle!+OR+cooperat!+OR+collaborat!+OR+disput!+OR+conflict!+OR+disagree!+OR+sanction!+OR+war+OR+troops+OR+%22letter+of+protest%22+OR+hostility+OR+%22shots+fired%22+OR+boycott+OR+protest!+OR+appeal+OR+intent+OR+reject+OR+threat!+OR+force+OR+coerce+OR+assault+OR+fight+OR+demand+OR+disapprove+OR+diploma!+OR+statement+OR+memorandum)+and+hlead('
    first_level_page_part_two = ')+and+not+hlead(ocean+OR+navigat!+OR+nuclear+OR+%22water+cannon%22+OR+%22light+water+reactor%22+OR+%22mineral+water%22+OR+%22hold+water%22+OR+%22cold+water%22+OR+%22hot+water%22+OR+%22water+canister%22+OR+%22water+tight%22+OR+%22+water+down%22+OR+%22flood+of+refugees%22+OR+Rivera+OR+Suez+OR+Panama+OR+oil+OR+drugs+OR+%22three+gorges%22+OR+waterski+OR+watermelon+OR+dishwater+OR+waterproof+OR+%22water+resistant%E2%80%9D+OR+%22water+bath%22)&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=undefined%7Calldates&pdfromadvancedsearchpage=true&ecomp=yxLg9kk&earg=pdpsf&prid=9e480b29-a32c-4d80-a750-04f0297661a9'
    first_level_page = first_level_page_part_one + search_terms + first_level_page_part_two

    driver.get(landing_page)
    time.sleep(4)
    driver.get(first_level_page)
    time.sleep(4)
    print("#STEP 1: Finished")

    time.sleep(60)
    

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

#Function 2: Login a User
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
    time.sleep(8)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(20)
    #driver.find_element(By.CSS_SELECTOR, ".advanced-search").click()
    print("login: was run you can now start the search")
  
def get_result_count():
    result_count_raw = driver.find_element(By.CSS_SELECTOR, ".countrendered")
    result_count = result_count_raw.text

    time.sleep(6)
    
    return result_count

    
    for i in range(4,0,-1):
        print(str(i)+'0 seconds left')
        time.sleep(10)
    print("done")
    

'''