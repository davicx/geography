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


#MAIN 
def main():
    if logged_in == False:
        login()
    else: 
        login_inside()
        single_basin_search()

#STEP 1: Navigate to Single Search (Includes Dates)
def single_basin_search():
  
    landing_page = 'https://advance-lexis-com.oregonstate.idm.oclc.org/bisacademicresearchhome/?pdmfid=1516831&crid=0f1105ae-7bcf-49e0-b0bd-1f5d6657e6ec&ecomp=zxryk&prid=86dd402e-b3c1-43d7-a5b0-308dbc0270c9'
    driver.get(landing_page)
    time.sleep(2)

    first_search_page = "https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=330256b4-b95a-444d-b900-b1f7b2980c2f&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(*water*+OR+river*+OR+lake+OR+dam+OR+stream+OR+tributary+OR+diversion+OR+irrigation+OR+pollution+OR+water+quality+OR+flood!+OR+drought!+OR+channel+OR+canal+OR+hydroelect!+OR+reservoir+OR+groundwater+OR+aquifer+OR+drought+OR+recharge+OR+%22water+table%22+OR+%22bore+hole)+and+treaty+OR+agree!+OR+negotiat!+OR+resolution+OR+commission+OR+secretariat+OR+joint+management+OR+basin+management+OR+peace+OR+accord+OR+%22peace+accord%22+OR+settle!+OR+cooperat!+OR+collaborat!+OR+disput!+OR+conflict!+OR+disagree!+OR+sanction!+OR+war+OR+troops+OR+%22letter+of+protest%22+OR+hostility+OR+%22shots+fired%22+OR+boycott+OR+protest!+OR+appeal+OR+intent+OR+reject+OR+threat!+OR+force+OR+coerce+OR+assault+OR+fight+OR+demand+OR+disapprove+OR+diploma!+OR+statement+OR+memorandum+and+not+ocean+OR+navigat!+OR+nuclear+OR+%22water+cannon%22+OR+%22light+water+reactor%22+OR+%22mineral+water%22+OR+%22hold+water%22+OR+%22cold+water%22+OR+%22hot+water%22+OR+%22water+canister%22+OR+%22water+tight%22+OR+%22+water+down%22+OR+%22flood+of+refugees%22+OR+Rivera+OR+Suez+OR+Panama+OR+oil+OR+drugs+OR+%22three+gorges%22+OR+waterski+OR+watermelon+OR+dishwater+OR+waterproof+OR+%E2%80%9Cwater+resistant%E2%80%9D+OR+%E2%80%9Cwater+bath%E2%80%9D&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=06%2F30%2F2008to03%2F22%2F2023%7Cdatebetween&pdfromadvancedsearchpage=true&ecomp=3xLg9kk&earg=pdpsf&prid=153fe97e-5ce8-418b-87cd-a3f208414f09"
    driver.get(first_search_page)
    print("Got it!")
    time.sleep(8)

    driver.get("https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=330256b4-b95a-444d-b900-b1f7b2980c2f&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(*water*+OR+river*+OR+lake+OR+dam+OR+stream+OR+tributary+OR+diversion+OR+irrigation+OR+pollution+OR+water+quality+OR+flood!+OR+drought!+OR+channel+OR+canal+OR+hydroelect!+OR+reservoir+OR+groundwater+OR+aquifer+OR+drought+OR+recharge+OR+%22water+table%22+OR+%22bore+hole)+and+treaty+OR+agree!+OR+negotiat!+OR+resolution+OR+commission+OR+secretariat+OR+joint+management+OR+basin+management+OR+peace+OR+accord+OR+%22peace+accord%22+OR+settle!+OR+cooperat!+OR+collaborat!+OR+disput!+OR+conflict!+OR+disagree!+OR+sanction!+OR+war+OR+troops+OR+%22letter+of+protest%22+OR+hostility+OR+%22shots+fired%22+OR+boycott+OR+protest!+OR+appeal+OR+intent+OR+reject+OR+threat!+OR+force+OR+coerce+OR+assault+OR+fight+OR+demand+OR+disapprove+OR+diploma!+OR+statement+OR+memorandum+and+not+ocean+OR+navigat!+OR+nuclear+OR+%22water+cannon%22+OR+%22light+water+reactor%22+OR+%22mineral+water%22+OR+%22hold+water%22+OR+%22cold+water%22+OR+%22hot+water%22+OR+%22water+canister%22+OR+%22water+tight%22+OR+%22+water+down%22+OR+%22flood+of+refugees%22+OR+Rivera+OR+Suez+OR+Panama+OR+oil+OR+drugs+OR+%22three+gorges%22+OR+waterski+OR+watermelon+OR+dishwater+OR+waterproof+OR+%E2%80%9Cwater+resistant%E2%80%9D+OR+%E2%80%9Cwater+bath%E2%80%9D&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=06%2F30%2F2008to03%2F22%2F2023%7Cdatebetween&pdfromadvancedsearchpage=true&ecomp=3xLg9kk&earg=pdpsf&prid=153fe97e-5ce8-418b-87cd-a3f208414f09")

    download_file_name = "ResultsList2"

    driver.find_element(By.CSS_SELECTOR, ".has_tooltip:nth-child(1) > .la-Download").click()
    time.sleep(5)

    driver.find_element(By.ID, "SelectedRange").click()
    driver.find_element(By.ID, "SelectedRange").send_keys("1-100")
    time.sleep(2)
    
    driver.find_element(By.ID, "FileName").send_keys("fileName")
    time.sleep(.5)
    driver.find_element(By.ID, "FileName").clear()
    time.sleep(2)

    driver.find_element(By.ID, "FileName").click()
    driver.find_element(By.ID, "FileName").send_keys(download_file_name)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".button-group > .primary").click()

    print("Pausing for download to finish")
    time.sleep(60)
  


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


    '''
driver.set_window_size(1636, 737)
element = driver.find_element(By.CSS_SELECTOR, ".overflow:nth-child(11) span > span:nth-child(1)")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element, 0, 0).perform()
driver.find_element(By.CSS_SELECTOR, ".has_tooltip:nth-child(1) > .la-Download").click()
driver.find_element(By.ID, "SelectedRange").click()
driver.find_element(By.ID, "SelectedRange").send_keys("1-100")
driver.find_element(By.CSS_SELECTOR, ".button-group > .primary").click()
'''




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
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(6)
    #driver.find_element(By.CSS_SELECTOR, ".advanced-search").click()
    print("login: was run you can now start the search")
  

if __name__ == "__main__":
    main()



#DOWNLOAD: EXCEL 
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

    '''
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
  
    '''
    print("STEP 3: Excel Downloads for ", basin_code, " FINISHED")
    time.sleep(1)


