from selenium import webdriver
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

PATH = "/Users/david/Desktop/David/www/development/geography/chromedriver.exe"
driver = webdriver.Chrome(PATH, options=options)


def main():
    login()
    first_level_search()
    second_level_search()
    download_results()

def login():
    print("STEP 1: Login") 
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
    time.sleep(12)
    driver.find_element(By.CSS_SELECTOR, ".advanced-search").click()
    print("login: was run moving to first level search")
    time.sleep(12)

def first_level_search():
    print("STEP 2: First Level Search") 
    searchLink = "https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=1c45062b-b31a-4c69-ac7d-2d5c3c7c33b5&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(box1)+and+hlead(box2)+and+not+hlead(box3)&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=12%2F08%2F2000to12%2F08%2F2022%7Cdatebetween&pdfromadvancedsearchpage=true&ecomp=3xLg9kk&earg=pdpsf&prid=ed3fc566-6534-4898-8343-4763b6de7c5f"

    driver.get(searchLink)
    time.sleep(12)

    #Turn duplicates on 
    driver.find_element(By.CSS_SELECTOR, ".custom-control-indicator").click()
    print("custom-control-indicator clicked")
    time.sleep(12)

def second_level_search():							
    print("STEP 3: Second Level Search") 

def download_results():
    print("STEP 4: Download results") 
    time.sleep(360)


if __name__ == "__main__":
    main()
