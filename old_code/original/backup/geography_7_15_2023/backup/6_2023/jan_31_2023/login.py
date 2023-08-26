from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import pandas as pd
import time

options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")
options.add_argument("user-data-dir=/tmp/david")
#options.add_argument("user-data-dir=/Users/david/Library/Caches/Google/chrome")

PATH = "/Users/david/Desktop/David/www/development/geography/chromedriver.exe"
driver = webdriver.Chrome(PATH, options=options)

logged_in = False


def main():
    full()
    #logged_in()
    #login()

def login():
    print("Opening login screen, please login with Duo")
    driver.get("https://library.oregonstate.edu/")
    time.sleep(5)
    element = driver.find_element(By.ID,"term-1search")
    element.send_keys("nexis uni")
    element.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#SEARCH_RESULT_RECORDID_alma99492178701865 mark").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".item-title:nth-child(1)").click()
    time.sleep(12)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(60)    

def login_user():
    driver.get("https://search.library.oregonstate.edu/discovery/search?vid=01ALLIANCE_OSU:OSU&tab=Everything&search_scope=OSU_Everything_Profile&lang=en&offset=0&query=any,contains,hi&displayField=all")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#signInBtn > span").click()
    time.sleep(5)
    element = driver.find_element(By.CSS_SELECTOR, ".md-focused")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".md-focused").click()
    time.sleep(5)
    driver.find_element(By.ID, "username").send_keys("vasquezd")
    driver.find_element(By.NAME, "_eventId_proceed").click()
    time.sleep(120)

def full():
    driver.get("https://library.oregonstate.edu/")
    time.sleep(3)
    element = driver.find_element(By.ID,"term-1search")
    element.send_keys("nexis uni")
    element.send_keys(Keys.RETURN)
    time.sleep(8)
    driver.find_element(By.CSS_SELECTOR, "#SEARCH_RESULT_RECORDID_alma99492178701865 mark").click()
    print("1")
    time.sleep(8)
    driver.find_element(By.CSS_SELECTOR, ".item-title:nth-child(1)").click()
    time.sleep(12)
    print("2")

    driver.switch_to.window(driver.window_handles[1])
    print("3")

    driver.find_element(By.CSS_SELECTOR, ".advanced-search").click()
    time.sleep(15)
    print("4")

    #Navigate to the first level search and move to this new tab 
    boxOne = "*water* OR river* OR lake OR dam OR stream OR tributary OR diversion OR irrigation OR pollution OR water quality OR flood! OR drought! OR channel OR canal OR hydroelect! OR   OR groundwater OR aquifer OR drought OR recharge OR water table OR bore hole"
    boxTwo = "treaty OR agree! OR negotiat! OR resolution OR commission OR secretariat OR joint management OR basin management OR peace OR accord OR peace accord OR settle! OR cooperat! OR collaborat! OR disput! OR conflict! OR disagree! OR sanction! OR war OR troops OR letter of protest OR hostility OR shots fired OR boycott OR protest! OR appeal OR intent OR reject OR threat! OR force OR coerce OR assault OR fight OR demand OR disapprove OR diploma! OR statement OR memorandum"
    boxThree = "ocean OR navigat! OR nuclear OR water cannon OR light water reactor OR mineral water OR hold water OR cold water OR hot water OR water canister OR water tight OR water down OR flood of refugees OR Rivera OR Suez OR Panama OR oil OR drugs OR three gorges OR waterski OR watermelon OR dishwater OR waterproof OR water resistant OR water bath"
    searchLink = "https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=1c45062b-b31a-4c69-ac7d-2d5c3c7c33b5&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(box1)+and+hlead(box2)+and+not+hlead(box3)&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=12%2F08%2F2000to12%2F08%2F2022%7Cdatebetween&pdfromadvancedsearchpage=true&ecomp=3xLg9kk&earg=pdpsf&prid=ed3fc566-6534-4898-8343-4763b6de7c5f"
    #searchLink = "https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=1c45062b-b31a-4c69-ac7d-2d5c3c7c33b5&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(stream)+and+hlead(water)+and+not+hlead(Panama)&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=12%2F08%2F2000to12%2F08%2F2022%7Cdatebetween&pdfromadvancedsearchpage=true&ecomp=3xLg9kk&earg=pdpsf&prid=ed3fc566-6534-4898-8343-4763b6de7c5f"

    driver.get(searchLink)
    time.sleep(10)
    print("5")

    #Turn duplicates on 
    driver.find_element(By.CSS_SELECTOR, ".custom-control-indicator").click()
    time.sleep(5)
    print("6")
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,103)")

    #second Level Search 
    #secondSearchTerm = "IB_FDDBasinNames"
    time.sleep(12)
    secondSearchTerm = "box1"
    print("7")
    driver.find_element(By.ID, "zz2yk_search").click()
    print("8")
    time.sleep(10)
    driver.find_element(By.ID, "zz2yk_search").send_keys(secondSearchTerm)
    print("9")
    #driver.find_element(By.ID, "zz2yk_search").click()
    #driver.find_element(By.ID, "zz2yk_search").send_keys("startsearchwithinresults")
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, ".src-submit").click()

    time.sleep(12)

    driver.find_element(By.CSS_SELECTOR, ".has_tooltip:nth-child(1) > .la-Download").click()
    time.sleep(12)
    driver.find_element(By.ID, "SelectedRange").click()
    driver.find_element(By.ID, "SelectedRange").send_keys("1-10")
    time.sleep(2)
    driver.find_element(By.ID, "FileName").click()
    driver.find_element(By.ID, "FileName").send_keys("myname")
    time.sleep(12)
    driver.find_element(By.CSS_SELECTOR, ".button-group > .primary").click()
    time.sleep(120)


def logged_in():
    driver.get("https://search.library.oregonstate.edu/discovery/search?vid=01ALLIANCE_OSU:OSU&tab=Everything&search_scope=OSU_Everything_Profile&lang=en&offset=0&query=any,contains,hi&displayField=all")    
    time.sleep(120)




if __name__ == "__main__":
    main()



'''





driver.find_element(By.CSS_SELECTOR, ".advanced-search").click()
time.sleep(15)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import pandas as pd
import time

logged_in = False

def main():
    if logged_in == False:
        login_user()
    else:   
        first_level_search()
        second_level_search()
        download_results()
 
def login_user():
    print("Opening login screen, please login with Duo")
    
def first_level_search():
    print("STEP 1: First Level Search") 
    data = pd.read_csv('data/firstLevelSearch.csv')

    for index, row in data.iterrows():
        field_one_search_terms = row['field_one'].replace(" ", "+")
        field_two_search_terms = row['field_two'].replace(" ", "+")
        field_three_search_terms = row['field_three'].replace(" ", "+")

    print(field_one_search_terms)
    print("")
    print(field_two_search_terms)
    print("")
    print(field_three_search_terms)
    first_search_url = "https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=c753d4b1-4bcb-4d62-bc2b-e5488b2cca1d&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(" + field_one_search_terms + ")+and+hlead(" + field_two_search_terms + ")+and+not+hlead(" + field_three_search_terms + ")&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=06%2F30%2F2008to01%2F10%2F2023%7Cdatebetween&pdfromadvancedsearchpage=true&ecomp=3xLg9kk&earg=pdpsf&prid=3c1ebaf8-b772-4481-a033-9d93018ce1b8"
    #print(first_search_url)


def second_level_search():							
    print("Second Level")
    dataSecondLevel = pd.read_csv('data/secondLevelSearch.csv')

    for index, row in dataSecondLevel.iterrows():
        basin_count = row['basin_count']
        search_type = row['search_type']
        search_terms = row['search_terms'].replace(" ", "+")
        basin_code = row['basin_code']
        basin_name = row['basin_name']
        ra_name = row['ra_name']
        search_completed = row['search_completed']
        preliminary_search = row['preliminary_search']
        notes = row['notes']
        print("BASIN NAME " + basin_name)
        print(search_terms)
        print("")

def download_results():
    print("Download results") 


if __name__ == "__main__":
    main()

'''