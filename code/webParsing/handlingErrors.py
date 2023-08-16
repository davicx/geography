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
from selenium.webdriver.common.alert import Alert

import os
import pandas as pd
import time

options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")
options.add_argument("user-data-dir=/tmp/david")
#prefs = {'download.default_directory' : '/Users/dvas22/Desktop/David/www/geography/web_page/downloads'}
prefs = {'download.default_directory' : '/Users/david/Desktop/David/www/geography/web_page/downloads'}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(options=options)

landing_page = "file:///Users/david/Desktop/David/www/geography/web_page/index.html"
driver.get(landing_page)

'''
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : '/path/to/dir'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
'''

def main():
    #element_id = "element-id"
    #text_id = "text-id"
    #alert_id = "alert-id"
    
    #find_element(element_id)
    #send_text(text_id)
    #click_button(alert_id)
    #find_item()
    #print("Finished!")
    #for x in range(6):
    #    print(x)

    download_files()
    time.sleep(30)

def download_files():
    print("TYPE 3: Click a button")
    count = 0

    while count < 2:
        try:
            time.sleep(1)
            click_element = driver.find_element(By.ID, "download-zip")
            time.sleep(1)  
            click_element.click()
            time.sleep(2)  
            count = 2

        except NoSuchElementException:  
            print("didnt work ", count)
            time.sleep(2)
            count = count + 1
            pass
        
    print("Finished 3")
    

#TYPE 1: Find an Element
def find_element(element_id): 
    print("TYPE 1: Find an Element")
    count = 0

    while count < 5:
        try:
            text_element = driver.find_element(By.ID, element_id).text
            print("We found the element with the text: ")
            print(text_element)
            time.sleep(30)  
            count = 2
        except NoSuchElementException:  
            print("didnt work ", count)
            count = count + 1
            time.sleep(2)
            pass

#TYPE 2: Send Text
def send_text(text_id): 
    print("TYPE 2: Send Text")
    count = 0

    while count < 2:
        try:
            send_element = driver.find_element(By.ID, text_id)
            send_element.clear()
            time.sleep(.5)
            send_element.send_keys("say hi!")
            time.sleep(2)
            count = 2
        except NoSuchElementException:  
            print("didnt work ", count)
            count = count + 1
            pass
    print("Finished 2")

#TYPE 3: Click a button
def click_button(button_id): 
    print("TYPE 3: Click a button")
    count = 0

    while count < 2:
        try:
            click_element = driver.find_element(By.ID, button_id)
            click_element.click()
            time.sleep(2)  
            Alert(driver).dismiss()
            time.sleep(2)  
            count = 2
        except NoSuchElementException:  
            print("didnt work ", count)
            count = count + 1
            pass
    print("Finished 3")

#TYPE 4: Find embedded item
def find_item():
    print("TYPE 4: Find embedded item")
    count = 0

    while count < 2:
        try:
            button = driver.find_element("xpath", "//ul[@class='filters-used']/li[2]/button")
            time.sleep(.5)  
            button.click()
            time.sleep(2)  
            Alert(driver).dismiss()
            print("Found!")
            time.sleep(1)  
            break
        except NoSuchElementException:  
            print("didnt work ", count)
            count = count + 1
            time.sleep(1)
            pass
    print("Finished 4")


if __name__ == "__main__":
    main()