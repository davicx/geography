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
from selenium import webdriver
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

logged_in = False

#MAIN:
def main():
    login()


def login():
    print("Login") 
    driver.get("https://library.oregonstate.edu/")
    time.sleep(5)

    element = driver.find_element(By.ID,"term-1search")
    element.send_keys("nexis uni")
    element.send_keys(Keys.RETURN)
    time.sleep(8)
    
    
    
    count = 0

    while count < 5:
        try:
            driver.find_element(By.CSS_SELECTOR, "#SEARCH_RESULT_RECORDID_alma99492178701865 markXXXX").click()
            time.sleep(1)
            
        except NoSuchElementException:
            print("exception handled total: ", count)
            count = count + 1
            time.sleep(1)

    print("now work")
    driver.find_element(By.CSS_SELECTOR, "#SEARCH_RESULT_RECORDID_alma99492178701865 mark").click()

    time.sleep(8)
    driver.find_element(By.CSS_SELECTOR, ".item-title:nth-child(1)").click()
    time.sleep(12)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(720)
    driver.find_element(By.CSS_SELECTOR, ".advanced-search").click()
    print("login: was run you can now start the search")
    time.sleep(720)

    '''
    print("Login") 
    driver.get("https://library.oregonstate.edu/")
    time.sleep(2)

    element = driver.find_element(By.ID,"term-1search")
    time.sleep(2)
    element.send_keys("nexis uni")
    element.send_keys(Keys.RETURN)
    time.sleep(2)

    count = 0

    while count < 5:
        try:
            driver.find_element(By.CSS_SELECTOR, "#SEARCH_RESULT_RECORDID_alma99492178701865 mark").click()
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, ".item-title:nth-child(1)").click()
        except NoSuchElementException:
            print("exception handled total: ", count)
            count = count + 1
            time.sleep(1)
    
    '''
    
    #driver.find_element(By.CSS_SELECTOR, ".item-title:nth-child(1)").click()
    #time.sleep(12)

    #driver.switch_to.window(driver.window_handles[1])
    #time.sleep(720)
    #driver.find_element(By.CSS_SELECTOR, ".advanced-search").click()
    #print("login: was run you can now start the search")
    time.sleep(720)
 
if __name__ == "__main__":
    main()