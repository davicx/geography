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
from selenium.webdriver.common.alert import Alert
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


def try_to_do(elementID):
    landing_page = "file:///Users/david/Desktop/David/www/geography/test.html"
    time.sleep(1) 
    driver.get(landing_page)
    time.sleep(2)
    
    #Find Element
    count = 0

    while count < 2:
        try:
            text_element = driver.find_element(By.ID, elementID).text
            print(text_element)
            time.sleep(1)  
            count = 2
        except NoSuchElementException:  
            print("didnt work ", count)
            count = count + 1
            pass

    #send_element = driver.find_element(By.ID, "name")
    #send_element.clear()
    #send_element.send_keys("say hi!")
    time.sleep(1)


def first_level_search():
    landing_page = "file:///Users/david/Desktop/David/www/geography/test.html"
    time.sleep(1) 
    driver.get(landing_page)
    time.sleep(2)
    
    #Find Element
    text_element = driver.find_element(By.ID, "hiya").text
    print(text_element)
    time.sleep(1)

    #Send Text
    send_element = driver.find_element(By.ID, "name")
    send_element.clear()
    send_element.send_keys("say hi!")
    time.sleep(1)

    #Click Button
    click_element = driver.find_element(By.ID, "click")
    click_element.click()
    time.sleep(2)
    Alert(driver).dismiss()

    #Send Text
    send_element = driver.find_element(By.ID, "name")
    send_element.clear()
    send_element.send_keys("say hi again!!")

    time.sleep(360)


#first_level_search()
'''
for x in range(5):
    print("Trying ", x)
    
    if x < 3:
        elementID = "hiyaOH"
    else: 
        elementID = "hiya"

    try_to_do(elementID)
    #send_element.send_keys("say hi!")

'''

def click_button():
    landing_page = "file:///Users/david/Desktop/David/www/geography/test.html"
    driver.get(landing_page)
    print("made it to landing page")
    #time.sleep(4)
    
    

    #Find Element
    count = 0

    while count < 2:
        try:
            button = driver.find_element("xpath", "//ul[@class='filters-used']/li[2]/button")
            button.click()
            print("Found!")
            time.sleep(1)  
            count = 2
        except NoSuchElementException:  
            print("didnt work ", count)
            count = count + 1
            time.sleep(1)
            pass



            '''
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul#ulBirthYear a[data-value='2002']")))
            element.click()
            '''

    #send_element = driver.find_element(By.ID, "name")
    #send_element.clear()
    #send_element.send_keys("say hi!")
    time.sleep(1)

click_button()
time.sleep(60)

'''
from selenium.common.exceptions import NoSuchElementException

try:
    elem = driver.find_element_by_xpath(".//*[@id='SORM_TB_ACTION0']")
    elem.click()
except NoSuchElementException:  #spelling error making this code not work as expected
    pass

elem = driver.find_elements_by_xpath(".//*[@id='SORM_TB_ACTION0']")
if len(elem) > 0
    elem[0].click()
'''