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

#Need to fix basin code and search term

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





date_one = "https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=aeca1622-8061-4f65-b8df-644573d56486&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(*water*+OR+river*+OR+lake+OR+dam+OR+stream+OR+tributary+OR+diversion+OR+irrigation+OR+pollution+OR+water+quality+OR+flood!+OR+drought!+OR+channel+OR+canal+OR+hydroelect!+OR+reservoir+OR+groundwater+OR+aquifer+OR+drought+OR+recharge+OR+%22water+table%22+OR+%22bore+hole+)+and+hlead(treaty+OR+agree!+OR+negotiat!+OR+resolution+OR+commission+OR+secretariat+OR+joint+management+OR+basin+management+OR+peace+OR+accord+OR+%22peace+accord%22+OR+settle!+OR+cooperat!+OR+collaborat!+OR+disput!+OR+conflict!+OR+disagree!+OR+sanction!+OR+war+OR+troops+OR+%22letter+of+protest%22+OR+hostility+OR+%22shots+fired%22+OR+boycott+OR+protest!+OR+appeal+OR+intent+OR+reject+OR+threat!+OR+force+OR+coerce+OR+assault+OR+fight+OR+demand+OR+disapprove+OR+diploma!+OR+statement+OR+memorandum)+and+not+ocean+OR+navigat!+OR+nuclear+OR+%22water+cannon%22+OR+%22light+water+reactor%22+OR+%22mineral+water%22+OR+%22hold+water%22+OR+%22cold+water%22+OR+%22hot+water%22+OR+%22water+canister%22+OR+%22water+tight%22+OR+%22+water+down%22+OR+%22flood+of+refugees%22+OR+Rivera+OR+Suez+OR+Panama+OR+oil+OR+drugs+OR+%22three+gorges%22+OR+waterski+OR+watermelon+OR+dishwater+OR+waterproof+OR+%22water+resistant%22+OR+%22water+bath%22&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=07%2F15%2F2009to07%2F14%2F2010%7Cdatebetween&pdfromadvancedsearchpage=true&ecomp=yxLg9kk&earg=pdpsf&prid=1a75d902-74df-40ac-9801-7493b8a82332"
date_two = "https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=74b80034-c505-4e16-a204-de4d4f1a9b16&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(*water*+OR+river*+OR+lake+OR+dam+OR+stream+OR+tributary+OR+diversion+OR+irrigation+OR+pollution+OR+water+quality+OR+flood!+OR+drought!+OR+channel+OR+canal+OR+hydroelect!+OR+reservoir+OR+groundwater+OR+aquifer+OR+drought+OR+recharge+OR+%22water+table%22+OR+%22bore+hole+)+and+hlead(treaty+OR+agree!+OR+negotiat!+OR+resolution+OR+commission+OR+secretariat+OR+joint+management+OR+basin+management+OR+peace+OR+accord+OR+%22peace+accord%22+OR+settle!+OR+cooperat!+OR+collaborat!+OR+disput!+OR+conflict!+OR+disagree!+OR+sanction!+OR+war+OR+troops+OR+%22letter+of+protest%22+OR+hostility+OR+%22shots+fired%22+OR+boycott+OR+protest!+OR+appeal+OR+intent+OR+reject+OR+threat!+OR+force+OR+coerce+OR+assault+OR+fight+OR+demand+OR+disapprove+OR+diploma!+OR+statement+OR+memorandum)+and+not+hlead(ocean+OR+navigat!+OR+nuclear+OR+%22water+cannon%22+OR+%22light+water+reactor%22+OR+%22mineral+water%22+OR+%22hold+water%22+OR+%22cold+water%22+OR+%22hot+water%22+OR+%22water+canister%22+OR+%22water+tight%22+OR+%22+water+down%22+OR+%22flood+of+refugees%22+OR+Rivera+OR+Suez+OR+Panama+OR+oil+OR+drugs+OR+%22three+gorges%22+OR+waterski+OR+watermelon+OR+dishwater+OR+waterproof+OR+%22water+resistant%22+OR+%22water+bath%22)&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=07%2F15%2F2010to07%2F14%2F2011%7Cdatebetween&pdfromadvancedsearchpage=true&ecomp=yxLg9kk&earg=pdpsf&prid=1a75d902-74df-40ac-9801-7493b8a82332"
date_three = "https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=ddefc9ae-24ea-4edc-be89-b22b4a798adc&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(*water*+OR+river*+OR+lake+OR+dam+OR+stream+OR+tributary+OR+diversion+OR+irrigation+OR+pollution+OR+water+quality+OR+flood!+OR+drought!+OR+channel+OR+canal+OR+hydroelect!+OR+reservoir+OR+groundwater+OR+aquifer+OR+drought+OR+recharge+OR+%22water+table%22+OR+%22bore+hole+)+and+hlead(treaty+OR+agree!+OR+negotiat!+OR+resolution+OR+commission+OR+secretariat+OR+joint+management+OR+basin+management+OR+peace+OR+accord+OR+%22peace+accord%22+OR+settle!+OR+cooperat!+OR+collaborat!+OR+disput!+OR+conflict!+OR+disagree!+OR+sanction!+OR+war+OR+troops+OR+%22letter+of+protest%22+OR+hostility+OR+%22shots+fired%22+OR+boycott+OR+protest!+OR+appeal+OR+intent+OR+reject+OR+threat!+OR+force+OR+coerce+OR+assault+OR+fight+OR+demand+OR+disapprove+OR+diploma!+OR+statement+OR+memorandum+)+and+not+hlead(ocean+OR+navigat!+OR+nuclear+OR+%22water+cannon%22+OR+%22light+water+reactor%22+OR+%22mineral+water%22+OR+%22hold+water%22+OR+%22cold+water%22+OR+%22hot+water%22+OR+%22water+canister%22+OR+%22water+tight%22+OR+%22+water+down%22+OR+%22flood+of+refugees%22+OR+Rivera+OR+Suez+OR+Panama+OR+oil+OR+drugs+OR+%22three+gorges%22+OR+waterski+OR+watermelon+OR+dishwater+OR+waterproof+OR+%22water+resistant%22+OR+%22water+bath%22)&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=07%2F15%2F2011to07%2F14%2F2012%7Cdatebetween&pdfromadvancedsearchpage=true&ecomp=yxLg9kk&earg=pdpsf&prid=f7b30bbb-acc8-445f-bcaa-9d91cc9630ec"

dates = [date_one, date_two, date_three]

#MAIN 
def main():
    if logged_in == False:
        login()
    else: 
        login_inside()
        basin_code = "Aral"
        search_terms = "Aral OR Syr Daria OR Naryn OR Amu Daria OR Syr Darya OR Amu Darya OR Akhangaran OR Chirchik"
        print("START SINGLE BASIN SEARCH: Starting a search for the basin " + basin_code)
        single_basin_search(basin_code, search_terms)

#STEP 1: Navigate to Single Search (Includes Dates)
def single_basin_search(basin_code, search_terms):
    print("STEP 1: Looping over search terms by Year") 

    masterToDoFile = 'master_to_do/aral.csv'
    masterToDo = pd.read_csv(masterToDoFile)
    
    for index, row in masterToDo.iterrows():
        search_link = row['link']
        start_date = row['start_date']
        end_date = row['end_date']
        finished = row['finished']
        #over_thousand = row['over_thousand']

        if finished != 1:
            masterToDo.loc[index, ['finished']] = [1] 
    
            landing_page = 'https://advance-lexis-com.oregonstate.idm.oclc.org/bisacademicresearchhome/?pdmfid=1516831&crid=0f1105ae-7bcf-49e0-b0bd-1f5d6657e6ec&ecomp=zxryk&prid=86dd402e-b3c1-43d7-a5b0-308dbc0270c9'
            driver.get(landing_page)
            time.sleep(4)
            driver.get(search_link)
            time.sleep(4)
            search_by_year(basin_code, search_terms)

            #Mark Completed 
            df = pd.DataFrame(masterToDo)  
            df.to_csv(masterToDoFile)
            print("STEP 1: Finished a single year from ", start_date, " to ", end_date) 
            time.sleep(30)

        else:     
            print("The basin ", basin_code, " is already done so we are skipping")
            time.sleep(.2)
    '''
    '''

    '''

    for first_level_link in dates:
        landing_page = 'https://advance-lexis-com.oregonstate.idm.oclc.org/bisacademicresearchhome/?pdmfid=1516831&crid=0f1105ae-7bcf-49e0-b0bd-1f5d6657e6ec&ecomp=zxryk&prid=86dd402e-b3c1-43d7-a5b0-308dbc0270c9'
        driver.get(landing_page)
        time.sleep(4)
        driver.get(first_level_link)
        time.sleep(4)
        search_by_year(basin_code, search_terms)
        time.sleep(360)

    print("STEP 1: Finished year") 
    time.sleep(5)
    '''
def search_by_year(basin_code, search_terms):
    second_level_search(basin_code, search_terms)
    basin_result_count = check_excel_result_count(basin_code)
    download_excel(basin_code, basin_result_count)


#STEP 2: Navigate to Second Level Search 
def second_level_search(basin_code, search_terms):	
    print("STEP 2: Second Level Search") 
    driver.execute_script("window.scrollTo(0,103)")
    time.sleep(8)

    driver.find_element(By.CSS_SELECTOR, ".excludeContainer input").click()
    driver.find_element(By.NAME, "includeExcludeSearchTerm").click()
    driver.find_element(By.ID, "kmnyk_search").click()
    driver.find_element(By.ID, "kmnyk_search").send_keys(search_terms)
    driver.find_element(By.CSS_SELECTOR, ".src-submit").click()
    
    time.sleep(5)
    print("STEP 2: Finished") 

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












'''
///Users/dvas22/Desktop/David/www/geography/drivers/chromedriver
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_driver_binary = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
'''