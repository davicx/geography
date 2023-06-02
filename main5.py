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

#MAIN 
def main():
    if logged_in == False:
        login()
    else: 
        run_search()

#Main: Rull Full Search of All Basins
def run_search():
    masterToDoFile = 'data/testMasterBasinToDo.csv'
    masterToDo = pd.read_csv(masterToDoFile)
    
    for index, row in masterToDo.iterrows():
        search_terms = row['search_terms']
        basin_code = row['basin_code']
        finished = row['finished']

        if finished != 1:
            masterToDo.loc[index, ['finished']] = [1] 
            print("START SINGLE BASIN SEARCH: Starting a search for the basin " + basin_code)

            single_basin_search(basin_code, search_terms)
            
            #Mark Completed 
            #df = pd.DataFrame(masterToDo)  
            #df.to_csv(masterToDoFile)
  
            print("FINISH SINGLE BASIN SEARCH")
            print("_________________________________________")
            print(" ")
            time.sleep(1)
        else:     
            print("The basin ", basin_code, " is already done so we are skipping")
            time.sleep(.2)
        #time.sleep(360)


#Main: Run Search for a Single Basin 
def single_basin_search(basin_code, search_term):
    first_level_search()
    
    #driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()
    #driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()
    #driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()
    #driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()


    #second_level_search(search_term)

    #start_date = "01/01/2008"
    #stop_date = "01/01/2010"
    #set_date(start_date, stop_date)
    #current_basin_count = check_result_count(basin_count, basin_code)

    #download_results_one_excel(basin_code, basin_count)
    #download_results_two_pdf(basin_code, basin_count)

    time.sleep(360)


#STEP 1: Navigate to First Level Search 
def first_level_search():
    print("STEP 1: First Level Search") 

    landing_page = 'https://advance-lexis-com.oregonstate.idm.oclc.org/bisacademicresearchhome/?pdmfid=1516831&crid=0f1105ae-7bcf-49e0-b0bd-1f5d6657e6ec&ecomp=zxryk&prid=86dd402e-b3c1-43d7-a5b0-308dbc0270c9'
    time.sleep(6) 
    searchLink = "https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=330256b4-b95a-444d-b900-b1f7b2980c2f&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(*water*+OR+river*+OR+lake+OR+dam+OR+stream+OR+tributary+OR+diversion+OR+irrigation+OR+pollution+OR+water+quality+OR+flood!+OR+drought!+OR+channel+OR+canal+OR+hydroelect!+OR+reservoir+OR+groundwater+OR+aquifer+OR+drought+OR+recharge+OR+%22water+table%22+OR+%22bore+hole)+and+treaty+OR+agree!+OR+negotiat!+OR+resolution+OR+commission+OR+secretariat+OR+joint+management+OR+basin+management+OR+peace+OR+accord+OR+%22peace+accord%22+OR+settle!+OR+cooperat!+OR+collaborat!+OR+disput!+OR+conflict!+OR+disagree!+OR+sanction!+OR+war+OR+troops+OR+%22letter+of+protest%22+OR+hostility+OR+%22shots+fired%22+OR+boycott+OR+protest!+OR+appeal+OR+intent+OR+reject+OR+threat!+OR+force+OR+coerce+OR+assault+OR+fight+OR+demand+OR+disapprove+OR+diploma!+OR+statement+OR+memorandum+and+not+ocean+OR+navigat!+OR+nuclear+OR+%22water+cannon%22+OR+%22light+water+reactor%22+OR+%22mineral+water%22+OR+%22hold+water%22+OR+%22cold+water%22+OR+%22hot+water%22+OR+%22water+canister%22+OR+%22water+tight%22+OR+%22+water+down%22+OR+%22flood+of+refugees%22+OR+Rivera+OR+Suez+OR+Panama+OR+oil+OR+drugs+OR+%22three+gorges%22+OR+waterski+OR+watermelon+OR+dishwater+OR+waterproof+OR+%E2%80%9Cwater+resistant%E2%80%9D+OR+%E2%80%9Cwater+bath%E2%80%9D&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=06%2F30%2F2008to03%2F22%2F2023%7Cdatebetween&pdfromadvancedsearchpage=true&ecomp=3xLg9kk&earg=pdpsf&prid=153fe97e-5ce8-418b-87cd-a3f208414f09"
    driver.get(landing_page)
    time.sleep(5)
    driver.get(searchLink)

    #driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".toremove").click()
    time.sleep(2)
    searchLink = "https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=330256b4-b95a-444d-b900-b1f7b2980c2f&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(*water*+OR+river*+OR+lake+OR+dam+OR+stream+OR+tributary+OR+diversion+OR+irrigation+OR+pollution+OR+water+quality+OR+flood!+OR+drought!+OR+channel+OR+canal+OR+hydroelect!+OR+reservoir+OR+groundwater+OR+aquifer+OR+drought+OR+recharge+OR+%22water+table%22+OR+%22bore+hole)+and+treaty+OR+agree!+OR+negotiat!+OR+resolution+OR+commission+OR+secretariat+OR+joint+management+OR+basin+management+OR+peace+OR+accord+OR+%22peace+accord%22+OR+settle!+OR+cooperat!+OR+collaborat!+OR+disput!+OR+conflict!+OR+disagree!+OR+sanction!+OR+war+OR+troops+OR+%22letter+of+protest%22+OR+hostility+OR+%22shots+fired%22+OR+boycott+OR+protest!+OR+appeal+OR+intent+OR+reject+OR+threat!+OR+force+OR+coerce+OR+assault+OR+fight+OR+demand+OR+disapprove+OR+diploma!+OR+statement+OR+memorandum+and+not+ocean+OR+navigat!+OR+nuclear+OR+%22water+cannon%22+OR+%22light+water+reactor%22+OR+%22mineral+water%22+OR+%22hold+water%22+OR+%22cold+water%22+OR+%22hot+water%22+OR+%22water+canister%22+OR+%22water+tight%22+OR+%22+water+down%22+OR+%22flood+of+refugees%22+OR+Rivera+OR+Suez+OR+Panama+OR+oil+OR+drugs+OR+%22three+gorges%22+OR+waterski+OR+watermelon+OR+dishwater+OR+waterproof+OR+%E2%80%9Cwater+resistant%E2%80%9D+OR+%E2%80%9Cwater+bath%E2%80%9D&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=06%2F30%2F2008to03%2F22%2F2009%7Cdatebetween&pdfromadvancedsearchpage=true&ecomp=3xLg9kk&earg=pdpsf&prid=153fe97e-5ce8-418b-87cd-a3f208414f09"
    driver.get(searchLink)
    #driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()

    print("STEP 1: Finished") 
    time.sleep(5)

#STEP 2: Navigate to Second Level Search 
def second_level_search(search_terms):	
    print("STEP 2: Second Level Search") 
    #time.sleep(5)
    driver.execute_script("window.scrollTo(0,103)")
    time.sleep(8)
    second_search_term = search_terms

    driver.find_element(By.CSS_SELECTOR, ".excludeContainer input").click()
    driver.find_element(By.NAME, "includeExcludeSearchTerm").click()
    driver.find_element(By.ID, "kmnyk_search").click()
    driver.find_element(By.ID, "kmnyk_search").send_keys(second_search_term)
    driver.find_element(By.CSS_SELECTOR, ".src-submit").click()
    
    time.sleep(5)
    print("STEP 2: Finished") 

#STEP 3: Set Date (This will be looped over)    				
def set_date(start_date, stop_date):
    driver.find_element(By.ID, "sortbymenulabel").click()
    driver.find_element(By.CSS_SELECTOR, "#dropdownmenu > button:nth-child(4)").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > .la-CloseRemove").click()
    print("close")
    time.sleep(1)
    #driver.find_element(By.CSS_SELECTOR, ".min-val").click()
    #driver.find_element(By.CSS_SELECTOR, ".min-val").send_keys(start_date)
    time.sleep(1)
    element = driver.find_element(By.ID, "podfiltersbuttondatestr-news")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    #driver.find_element(By.CSS_SELECTOR, ".max-val").click()
    ##driver.find_element(By.CSS_SELECTOR, ".max-val").send_keys(stop_date)
    #driver.find_element(By.CSS_SELECTOR, ".save").click()
    time.sleep(1)

    #driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()
    '''
        element = driver.find_element(By.ID, "podfiltersbuttondatestr-news")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".min-val").click()
    driver.find_element(By.CSS_SELECTOR, ".min-val").send_keys(start_date)
    driver.find_element(By.CSS_SELECTOR, ".max-val").click()
    driver.find_element(By.CSS_SELECTOR, ".max-val").send_keys(stop_date)
    driver.find_element(By.CSS_SELECTOR, ".save").click()
    '''



#STEP 3: CHANGE Check the Basin Count and set the group results tab
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


#STEP 4: Download Excel (1000)
#Group Results
#Sort by Date (Oldest to Newest)

#DOWNLOAD (Loop by Year)
#STEP 3: Download Excel (1000)- I think we need to rename these 
#Step A: 1 Year Period
#Step B: Loop over download and paginate
#Step C: When done clear year and go to next year

#STEP 4: Download PDF (250)


#FUNCTIONS
#Function 1: Login a User
def login():
    print("Login") 
    driver.get("https://library.oregonstate.edu/")
    time.sleep(5)

    element = driver.find_element(By.ID,"term-1search")
    element.send_keys("nexis uni")
    element.send_keys(Keys.RETURN)
    time.sleep(15)
    driver.find_element(By.CSS_SELECTOR, "#SEARCH_RESULT_RECORDID_alma99492178701865 mark").click()
    time.sleep(8)
    driver.find_element(By.CSS_SELECTOR, ".item-title:nth-child(1)").click()
    time.sleep(12)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(720)
    driver.find_element(By.CSS_SELECTOR, ".advanced-search").click()
    print("login: was run you can now start the search")
    time.sleep(720)

if __name__ == "__main__":
    main()

'''
    self.driver.get("https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=330256b4-b95a-444d-b900-b1f7b2980c2f&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(*water*+OR+river*+OR+lake+OR+dam+OR+stream+OR+tributary+OR+diversion+OR+irrigation+OR+pollution+OR+water+quality+OR+flood!+OR+drought!+OR+channel+OR+canal+OR+hydroelect!+OR+reservoir+OR+groundwater+OR+aquifer+OR+drought+OR+recharge+OR+%22water+table%22+OR+%22bore+hole)+and+treaty+OR+agree!+OR+negotiat!+OR+resolution+OR+commission+OR+secretariat+OR+joint+management+OR+basin+management+OR+peace+OR+accord+OR+%22peace+accord%22+OR+settle!+OR+cooperat!+OR+collaborat!+OR+disput!+OR+conflict!+OR+disagree!+OR+sanction!+OR+war+OR+troops+OR+%22letter+of+protest%22+OR+hostility+OR+%22shots+fired%22+OR+boycott+OR+protest!+OR+appeal+OR+intent+OR+reject+OR+threat!+OR+force+OR+coerce+OR+assault+OR+fight+OR+demand+OR+disapprove+OR+diploma!+OR+statement+OR+memorandum+and+not+ocean+OR+navigat!+OR+nuclear+OR+%22water+cannon%22+OR+%22light+water+reactor%22+OR+%22mineral+water%22+OR+%22hold+water%22+OR+%22cold+water%22+OR+%22hot+water%22+OR+%22water+canister%22+OR+%22water+tight%22+OR+%22+water+down%22+OR+%22flood+of+refugees%22+OR+Rivera+OR+Suez+OR+Panama+OR+oil+OR+drugs+OR+%22three+gorges%22+OR+waterski+OR+watermelon+OR+dishwater+OR+waterproof+OR+%E2%80%9Cwater+resistant%E2%80%9D+OR+%E2%80%9Cwater+bath%E2%80%9D&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=06%2F30%2F2008to03%2F22%2F2010|datebetween&pdfromadvancedsearchpage=true&ecomp=3xLg9kk&earg=pdpsf&prid=153fe97e-5ce8-418b-87cd-a3f208414f09")
    self.driver.set_window_size(550, 691)
    element = self.driver.find_element(By.CSS_SELECTOR, ".gnslanguagebutton")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.execute_script("window.scrollTo(0,111)")
    self.driver.find_element(By.ID, "kmnyk_search").click()
    self.driver.find_element(By.ID, "kmnyk_search").send_keys("Aral OR Syr Daria OR Naryn OR Amu Daria OR Syr Darya OR Amu Darya OR Akhangaran OR Chirchik")
    self.driver.find_element(By.CSS_SELECTOR, ".src-submit").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.ID, "sortbymenulabel").click()
    self.driver.find_element(By.CSS_SELECTOR, "#dropdownmenu > button:nth-child(4)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > .la-CloseRemove").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()
    element = self.driver.find_element(By.ID, "podfiltersbuttondatestr-news")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".min-val").click()
    self.driver.find_element(By.CSS_SELECTOR, ".min-val").click()
    self.driver.find_element(By.CSS_SELECTOR, ".min-val").send_keys("01/01/2008")
    self.driver.find_element(By.CSS_SELECTOR, ".max-val").click()
    self.driver.find_element(By.CSS_SELECTOR, ".max-val").send_keys("01/01/2010")
    self.driver.find_element(By.CSS_SELECTOR, ".save").click()
    self.driver.execute_script("window.scrollTo(0,0)")
'''