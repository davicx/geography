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
prefs = {'download.default_directory' : '/Users/dvas22/Desktop/David/www/geography/downloads'}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

logged_in = True  


#MAIN 
def main():
    if logged_in == False:
        login()
    else: 
        #login_inside()
        basin_code = "Aral"
        search_terms = "Aral OR Syr Daria OR Naryn OR Amu Daria OR Syr Darya OR Amu Darya OR Akhangaran OR Chirchik"
        change_date(basin_code, search_terms, "01/01/2000", "02/01/2000")
        change_date(basin_code, search_terms, "02/01/2000", "03/01/2000")

#FUNCTION 1: Navigate to Single Search (Includes Dates)
def change_date(basin_code, search_terms, start_date, end_date):

    #STEP 1: Navigate to the landing Page
    landing_page = 'https://advance-lexis-com.oregonstate.idm.oclc.org/bisacademicresearchhome/?pdmfid=1516831&crid=0f1105ae-7bcf-49e0-b0bd-1f5d6657e6ec&ecomp=zxryk&prid=86dd402e-b3c1-43d7-a5b0-308dbc0270c9'
    search_link = "https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=ee3cdb2a-2939-41a3-a77f-becbd14288b6&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(*water*+OR+river*+OR+lake+OR+dam+OR+stream+OR+tributary+OR+diversion+OR+irrigation+OR+pollution+OR+water+quality+OR+flood!+OR+drought!+OR+channel+OR+canal+OR+hydroelect!+OR+reservoir+OR+groundwater+OR+aquifer+OR+drought+OR+recharge+OR+%22water+table%22+OR+%22bore+hole+)+and+hlead(treaty+OR+agree!+OR+negotiat!+OR+resolution+OR+commission+OR+secretariat+OR+joint+management+OR+basin+management+OR+peace+OR+accord+OR+%22peace+accord%22+OR+settle!+OR+cooperat!+OR+collaborat!+OR+disput!+OR+conflict!+OR+disagree!+OR+sanction!+OR+war+OR+troops+OR+%22letter+of+protest%22+OR+hostility+OR+%22shots+fired%22+OR+boycott+OR+protest!+OR+appeal+OR+intent+OR+reject+OR+threat!+OR+force+OR+coerce+OR+assault+OR+fight+OR+demand+OR+disapprove+OR+diploma!+OR+statement+OR+memorandum+)+and+ocean+OR+navigat!+OR+nuclear+OR+%22water+cannon%22+OR+%22light+water+reactor%22+OR+%22mineral+water%22+OR+%22hold+water%22+OR+%22cold+water%22+OR+%22hot+water%22+OR+%22water+canister%22+OR+%22water+tight%22+OR+%22+water+down%22+OR+%22flood+of+refugees%22+OR+Rivera+OR+Suez+OR+Panama+OR+oil+OR+drugs+OR+%22three+gorges%22+OR+waterski+OR+watermelon+OR+dishwater+OR+waterproof+OR+%E2%80%9Cwater+resistant%E2%80%9D+OR+%E2%80%9Cwater+bath%E2%80%9D&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=undefined%7Calldates&pdfromadvancedsearchpage=true&ecomp=yxLg9kk&earg=pdpsf&prid=87267cf8-b3ce-46d2-9888-e5ccc3c814bb"
    driver.get(landing_page)
    time.sleep(4)
    driver.get(search_link)
    time.sleep(4)
    driver.execute_script("window.scrollTo(0,80)")
    time.sleep(1)

    #STEP 2: Open the timeline 
    #May need to open and close if timeline selector value does not show up sometimes it loads slow or does not load
    timeline_opened = True

    if timeline_opened == False: 
        driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()
        time.sleep(8)


    #STEP 3: Set Minimum Value
    count = 0

    while count < 5:
        try:
            driver.find_element(By.CSS_SELECTOR, ".min-val").click()
            time.sleep(1)  
            count = 10 
        except NoSuchElementException:  
            print("NoSuchElementException couldn't find min value ", count)
            driver.get(search_link)
            time.sleep(4) 

            '''
            time.sleep(1) 
            driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()
            time.sleep(2)
            driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()
            time.sleep(4)  
            '''

            count = count + 1
    
    #Step 3A: Clear out the current minimum date
    for x in range(12):
        driver.find_element(By.CSS_SELECTOR, ".min-val").send_keys(Keys.BACKSPACE)
        time.sleep(.2)
    time.sleep(1)

    #Step 3B: Put the new date in
    driver.find_element(By.CSS_SELECTOR, ".min-val").send_keys(start_date)
    time.sleep(2)

    #STEP 4: Set Maximum Value
    try:
        driver.find_element(By.CSS_SELECTOR, ".max-val").click()
        time.sleep(1)   
    except NoSuchElementException:  
        driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()

    for x in range(12):
        driver.find_element(By.CSS_SELECTOR, ".max-val").send_keys(Keys.BACKSPACE)
        time.sleep(.2)   
    time.sleep(1)
 
    driver.find_element(By.CSS_SELECTOR, ".max-val").send_keys(end_date)
    time.sleep(2)
    
    driver.find_element(By.CSS_SELECTOR, ".save").click()
    
    #STEP 5: Wait
    time.sleep(15)



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

if __name__ == "__main__":
    main()
