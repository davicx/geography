#LOGIN: Example 1 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import os
import pandas as pd
import time

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/")

driver.get("https://www.google.com/")
time.sleep(3)

'''
#LOGIN: Example 2 
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
options.add_argument("user-data-dir=/tmp/selenawallace")
prefs = {'download.default_directory' : '/Users/selenawallace/Documents/Data_Science/geography'}
options.add_experimental_option('prefs', prefs)
options.add_experimental_option("detach", True) #keeps window open  

logged_in = True 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='114.0.5735.90').install()), options=options)

driver.get("https://www.google.com/")
time.sleep(3)
driver.find_element(By.ID, "APjFqb").send_keys("hello Chrome")
driver.find_element(By.ID, "APjFqb").send_keys(Keys.RETURN)
'''
