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
from selenium.common.exceptions import ElementNotInteractableException
from chromedriver_py import binary_path  

import os
import sys
import pandas as pd
import time

options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")
#options.add_argument("user-data-dir=/tmp/david")
options.add_argument("user-data-dir=/tmp/david2")
#prefs = {'download.default_directory' : '/Users/dvas22/Desktop/David/www/geography/downloads'}
prefs = {'download.default_directory' : '/Users/david/Desktop/David/www/geography/downloads/temp'}
options.add_experimental_option('prefs', prefs)
#options.add_experimental_option("detach", True)

#Driver Type 1: The two driver types are dependent on which computer setup this is running on
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#Driver Type 2: 
svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc, options=options)

#Set Tufts or External User 
external_user = True


def check_timeline_opened():
    timeline_opened = False

    try:
        min_val_temp = driver.find_element(By.CSS_SELECTOR, ".min-val")   
        timeline_opened = True
        print("The timeline is opened")
    except NoSuchElementException:  
        timeline_opened = False
        print("The timeline is not opened")
    return timeline_opened




#TIMELINE BUTTON
#Scroll to Position 
driver.execute_script("window.scrollTo(0,120)")
time.sleep(2)
driver.execute_script("window.scrollTo(0,400)")
time.sleep(2)

#check if timeline is opened
timeline_opened = check_timeline_opened()
print("First check on timeline ")
print(timeline_opened)

for x in range(1, 5):
    print("Opening total times ", x)
    timeline_opened = check_timeline_opened()
    print("Check on timeline again")
    print(timeline_opened)
    print(" ")

    if timeline_opened == False:
        print("The timeline is closed so we will open the timeline")

        #Open the Timeline
        try:
            driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()
            print("Found and opened the timeline")

            time.sleep(8)  
        except NoSuchElementException:  
            print("Couldn't find the timeline open button")

    else: 
        print("Timeline is opened")
        #Close the Timeline
        try:
            driver.find_element(By.ID, "podfiltersbuttondatestr-news").click()
            print("Found and opened the timeline")

            time.sleep(8)  
        except NoSuchElementException:  
            print("Couldn't find the timeline open button")

    timeline_opened = check_timeline_opened()
    print("Final check on timeline ")
    print(timeline_opened)

