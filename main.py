from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import time

options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")
options.add_argument("user-data-dir=/tmp/david")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


logged_in = True

def main():
    if logged_in == False:
        login()
    else: 
        first_level_search()
        second_level_search()
        get_result_count()
        download_results()


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

def first_level_search():
    print("STEP 1: First Level Search") 
    search_term_one = "box1"
    search_term_two = "box2"
    search_term_three = "box3"

    #searchLink = "https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=1c45062b-b31a-4c69-ac7d-2d5c3c7c33b5&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(box1)+and+hlead(box2)+and+not+hlead(box3)&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=12%2F08%2F2000to12%2F08%2F2022%7Cdatebetween&pdfromadvancedsearchpage=true&ecomp=3xLg9kk&earg=pdpsf&prid=ed3fc566-6534-4898-8343-4763b6de7c5f"
    searchLink = "https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=1c45062b-b31a-4c69-ac7d-2d5c3c7c33b5&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(" + search_term_one + ")+and+hlead(" + search_term_two + ")+and+not+hlead(" + search_term_three + ")&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=12%2F08%2F2000to12%2F08%2F2022%7Cdatebetween&pdfromadvancedsearchpage=true&ecomp=3xLg9kk&earg=pdpsf&prid=ed3fc566-6534-4898-8343-4763b6de7c5f"
    driver.get(searchLink)
    print("STEP 1: Finished") 
    time.sleep(12)

def second_level_search():							
    print("STEP 2: Second Level Search") 
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,103)")
    time.sleep(15)
    second_search_term = "BOX 1"

    driver.find_element(By.CSS_SELECTOR, ".excludeContainer input").click()
    driver.find_element(By.NAME, "includeExcludeSearchTerm").click()
    driver.find_element(By.ID, "zznyk_search").click()
    driver.find_element(By.ID, "zznyk_search").send_keys(second_search_term)
    driver.find_element(By.CSS_SELECTOR, ".src-submit").click()
    
    time.sleep(15)

    #Turn duplicates on (after first search this defaults to on)
    print("custom-control-indicator clicked")
    driver.find_element(By.CSS_SELECTOR, ".custom-control-indicator").click()
    time.sleep(12)
    print("STEP 2: Finished") 

def get_result_count():
    print("STEP 3: Get Results Count") 
    #result_count = driver.find_element(By.CSS_SELECTOR, ".resultsHeader > h2 > span")
    #print("Total Results ", result_count)
    #result_count = driver.find_element_by_css_selector(".ocenaCzastkowa.masterTooltip")
    result_count_raw = driver.find_element(By.CSS_SELECTOR, ".countrendered")
    #span_element.text time.sleep(360)
    result_count = result_count_raw.text

    print("result_count")
    print(result_count)
    
    time.sleep(12)
    
    print("STEP 3: Finished")   

def download_results():
    print("STEP 4: Download results") 
    for x in range(4): 
        driver.find_element(By.CSS_SELECTOR, ".has_tooltip:nth-child(1) > .la-Download").click()
        time.sleep(12)
        driver.find_element(By.CSS_SELECTOR, ".DeliveryItemType > .row:nth-child(3) > label").click()
        time.sleep(8)
        driver.find_element(By.CSS_SELECTOR, ".nested:nth-child(3) #SelectedRange").click()
        time.sleep(8)
        start_key = 1 + x
        end_key = 10 + x
        print(start_key)
        print(end_key)
        download = str(start_key) + "-" + str(end_key)
        print(download)

        '''
        self.driver.find_element(By.CSS_SELECTOR, ".has_tooltip:nth-child(1) > .la-Download").click()
        self.driver.find_element(By.ID, "SelectedRange").click()
        self.driver.find_element(By.ID, "SelectedRange").send_keys("1-10")
        self.driver.find_element(By.ID, "FileName").click()
        self.driver.find_element(By.ID, "FileName").send_keys("files_1_10")
        self.driver.find_element(By.CSS_SELECTOR, ".button-group > .primary").click()
        '''

        driver.find_element(By.CSS_SELECTOR, ".nested:nth-child(3) #SelectedRange").send_keys(download)
        driver.find_element(By.CSS_SELECTOR, ".Format > .row:nth-child(4)").click()
        time.sleep(5)
        driver.find_element(By.ID, "FileName").click()
        time.sleep(5)
        driver.find_element(By.ID, "FileName").send_keys("fileName")
        driver.find_element(By.ID, "FileName").clear()
        time.sleep(5)
        driver.find_element(By.ID, "FileName").send_keys("fileName")
        #driver.find_element_by_xpath("//input[class ='gsc-search']").clear()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, ".button-group > .primary").click()
        time.sleep(60)

        print("STEP 4: Finished")   
        print(x)


#WORKS
'''
def download_results():
    print("STEP 4: Download results") 
    driver.find_element(By.CSS_SELECTOR, ".has_tooltip:nth-child(1) > .la-Download").click()
    time.sleep(12)
    driver.find_element(By.CSS_SELECTOR, ".DeliveryItemType > .row:nth-child(3) > label").click()
    time.sleep(8)
    driver.find_element(By.CSS_SELECTOR, ".nested:nth-child(3) #SelectedRange").click()
    time.sleep(8)
    driver.find_element(By.CSS_SELECTOR, ".nested:nth-child(3) #SelectedRange").send_keys("1-10")
    driver.find_element(By.CSS_SELECTOR, ".Format > .row:nth-child(4)").click()
    time.sleep(5)
    driver.find_element(By.ID, "FileName").click()
    time.sleep(5)
    driver.find_element(By.ID, "FileName").send_keys("fileName")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".button-group > .primary").click()
    time.sleep(60)

    print("STEP 4: Finished")   
'''

if __name__ == "__main__":
    main()







#Turn duplicates on (after first search this defaults to on)
#driver.find_element(By.CSS_SELECTOR, ".custom-control-indicator").click()
#print("custom-control-indicator clicked")
#time.sleep(12)