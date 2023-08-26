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
pdfPath = '/Users/david/Desktop/David/www/geography/downloads/pdf/'
excelPath = '/Users/david/Desktop/David/www/geography/downloads/excel/'


#MAIN:
def main():
    if logged_in == False:
        login()
    else: 
        run_search()

#MAIN: Run full Search 
def run_search():
    data = pd.read_csv('data/singleBasinToDo.csv')
    
    for index, row in data.iterrows():
        search_terms = row['search_terms']
        basin_code = row['basin_code']
        basin_count = row['basin_count']
        search_completed = row['search_completed']
    
        print("START SINGLE BASIN SEARCH: Starting a search for the basin " + basin_code)
        print("Status: ", search_completed)
        single_basin_search(basin_code, search_terms, basin_count)
        print("FINISH SINGLE BASIN SEARCH")
        print("_________________________________________")
        print(" ")
        time.sleep(360)


#MAIN: Run Search for a Single Basin 
def single_basin_search(basin_code, search_term, basin_count):
    first_level_search()
    second_level_search(search_term)
    current_basin_count = check_result_count(basin_count, basin_code)

    download_results_one_excel(basin_code, basin_count)
    #download_results_two_pdf(basin_code, basin_count)

    time.sleep(5)

#STEP 1: Navigate to first level search 
def first_level_search():
    print("STEP 1: First Level Search") 

    landing_page = 'https://advance-lexis-com.oregonstate.idm.oclc.org/bisacademicresearchhome/?pdmfid=1516831&crid=0f1105ae-7bcf-49e0-b0bd-1f5d6657e6ec&ecomp=zxryk&prid=86dd402e-b3c1-43d7-a5b0-308dbc0270c9'
    time.sleep(6) 
    searchLink = "https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=330256b4-b95a-444d-b900-b1f7b2980c2f&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(*water*+OR+river*+OR+lake+OR+dam+OR+stream+OR+tributary+OR+diversion+OR+irrigation+OR+pollution+OR+water+quality+OR+flood!+OR+drought!+OR+channel+OR+canal+OR+hydroelect!+OR+reservoir+OR+groundwater+OR+aquifer+OR+drought+OR+recharge+OR+%22water+table%22+OR+%22bore+hole)+and+treaty+OR+agree!+OR+negotiat!+OR+resolution+OR+commission+OR+secretariat+OR+joint+management+OR+basin+management+OR+peace+OR+accord+OR+%22peace+accord%22+OR+settle!+OR+cooperat!+OR+collaborat!+OR+disput!+OR+conflict!+OR+disagree!+OR+sanction!+OR+war+OR+troops+OR+%22letter+of+protest%22+OR+hostility+OR+%22shots+fired%22+OR+boycott+OR+protest!+OR+appeal+OR+intent+OR+reject+OR+threat!+OR+force+OR+coerce+OR+assault+OR+fight+OR+demand+OR+disapprove+OR+diploma!+OR+statement+OR+memorandum+and+not+ocean+OR+navigat!+OR+nuclear+OR+%22water+cannon%22+OR+%22light+water+reactor%22+OR+%22mineral+water%22+OR+%22hold+water%22+OR+%22cold+water%22+OR+%22hot+water%22+OR+%22water+canister%22+OR+%22water+tight%22+OR+%22+water+down%22+OR+%22flood+of+refugees%22+OR+Rivera+OR+Suez+OR+Panama+OR+oil+OR+drugs+OR+%22three+gorges%22+OR+waterski+OR+watermelon+OR+dishwater+OR+waterproof+OR+%E2%80%9Cwater+resistant%E2%80%9D+OR+%E2%80%9Cwater+bath%E2%80%9D&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=06%2F30%2F2008to03%2F22%2F2023%7Cdatebetween&pdfromadvancedsearchpage=true&ecomp=3xLg9kk&earg=pdpsf&prid=153fe97e-5ce8-418b-87cd-a3f208414f09"
    driver.get(landing_page)
    time.sleep(5)
    driver.get(searchLink)
    print("STEP 1: Finished") 
    time.sleep(5)


#STEP 2: Navigate to first level search 
def second_level_search(search_terms):							
    print("STEP 2: Second Level Search") 
    #time.sleep(5)
    driver.execute_script("window.scrollTo(0,103)")
    time.sleep(8)
    second_search_term = search_terms

    driver.find_element(By.CSS_SELECTOR, ".excludeContainer input").click()
    driver.find_element(By.NAME, "includeExcludeSearchTerm").click()
    driver.find_element(By.ID, "-znyk_search").click()
    driver.find_element(By.ID, "-znyk_search").send_keys(second_search_term)
    driver.find_element(By.CSS_SELECTOR, ".src-submit").click()
    
    time.sleep(5)
    print("STEP 2: Finished") 

#STEP 3: Check the Basin Count and set the group results tab
def check_result_count(basin_count, basin_code):
    print("STEP 3: Check the Basin Count") 
    
    #Make sure that we group results
    basin_result_count_one = get_result_count()
    driver.find_element(By.CSS_SELECTOR, ".custom-control-indicator").click()
    time.sleep(5)
    basin_result_count_two = get_result_count()
    
    if basin_result_count_two > basin_result_count_one:
        driver.find_element(By.CSS_SELECTOR, ".custom-control-indicator").click()
        time.sleep(5)    

    print("Count 1- Input Basin Count: ", basin_count)
    print("Count 2- Current Page Count ", basin_result_count_two)
    print("Count 3- Current Page Count ", basin_result_count_two)
    basin_result_count = min(basin_result_count_one, basin_result_count_two)
    time.sleep(5)
    if basin_count == basin_result_count:
        print("Count Matches: basin result count ", basin_code, basin_result_count)
    else:
        print("Count Does not Match: this could cause an error it means the count has changed since we first checked")
        print("basin result count ", basin_code, basin_result_count)

    print("STEP 3: Finished ")


##DOWNLOAD DATA##
#STEP 4: Download Excel Results (Up to 1000) Naming file download works 
def download_results_one_excel(basin_code, basin_count):
    individualBasinToDoFile = 'data/singleBasinToDo/excel/' + basin_code + '.csv'
    
    print("STEP 4: Starting to Download all excel Results for Basin Code ", basin_code) 
   
    excelData = pd.read_csv(individualBasinToDoFile)

    for index, row in excelData.iterrows():
        basin_code = row['basin_code']
        min = row['min']
        max = row['max']
        finished = row['finished']
        
        if finished != 1:
            download_single_result_excel(basin_code, min, max)
            excelData.loc[index, ['finished']] = [1] 
            print("The data was downloaded marking complete")
            df = pd.DataFrame(excelData)  
            df.to_csv(individualBasinToDoFile)
            print("running search for ", basin_code, min, max, finished)
            time.sleep(1)
        else:     
            print("The basin ", basin_code, " from ", min, " to ", max, " is already done so we are skipping")
            time.sleep(.1)

        time.sleep(1)

    print("STEP 4: Finished") 
    #time.sleep(5)


#STEP 4A: Single Download a set of 1000 for Excel files
#/Users/david/Desktop/David/www/geography/downloads/excel/ARAL
def download_single_result_excel(basin_code, min, max):
    #max is 999
    max = max - 800
    min_int = int(min)
    min_int = int(max)
    min = str(min)
    max = str(max)
    print("Starting Downloads 1: Excel files for ", basin_code, ": from ", min, " to ", max)
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
    time.sleep(5)
    driver.find_element(By.ID, "FileName").send_keys("fileName")
    driver.find_element(By.ID, "FileName").clear()
    time.sleep(5)
    driver.find_element(By.ID, "FileName").send_keys(download_file_name)
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, ".button-group > .primary").click()
    print("Finished downloads from ", min, " to ", max)
    time.sleep(20)
    
    fileNameOriginal = path + download_file_name + ".ZIP"
    fileNameNew = path + basin_code + "/" + download_file_name + ".ZIP"
    os.rename(fileNameOriginal, fileNameNew)
    time.sleep(5)

    '''
    

    driver.find_element(By.CSS_SELECTOR, ".DeliveryItemType > .row:nth-child(3) > label").click()
    time.sleep(4)


    '''

#STEP 5: Download PDF Files (Up to 100)
def download_results_two_pdf(basin_code, basin_count):
    individualBasinToDoFile = 'data/singleBasinToDo/pdf/' + basin_code + '.csv'
    
    print("STEP 5: Starting to Download all pdf Results for Basin Code ", basin_code) 
   
    excelData = pd.read_csv(individualBasinToDoFile)

    for index, row in excelData.iterrows():
        basin_code = row['basin_code']
        min = row['min']
        max = row['max']
        finished = row['finished']
        
        if finished != 1:
            #run_search(index)
            excelData.loc[index, ['finished']] = [1] 
            print("The data was downloaded marking complete")
            df = pd.DataFrame(excelData)  
            df.to_csv(individualBasinToDoFile)
            print("running search for ", basin_code, min, max, finished)
            time.sleep(1)
        else:     
            print("The basin ", basin_code, " from ", min, " to ", max, " is already done so we are skipping")
            time.sleep(1)

        time.sleep(1)

    print("STEP 5: Finished") 




#NOT DONE BELOW




#CLEAN BELOW
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

    


#STEP 4: Download First Results of Excel Files (this can be slow)
def download_results_two_pdf_old(basin_code, basin_result_count):
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

#HELPER FUNCTIONS
def get_result_count():
    result_count_raw = driver.find_element(By.CSS_SELECTOR, ".countrendered")
    result_count = result_count_raw.text

    time.sleep(6)
    
    print("STEP 3: Finished")  
    return result_count

def create_download_folder(basin_code):
    newpath = '/Users/david/Desktop/David/www/geography/downloads/' +  basin_code
    if not os.path.exists(newpath):
        os.makedirs(newpath)
