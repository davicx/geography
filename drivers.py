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


#DRIVER
#Driver Type 1: 
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")

#options.add_argument("user-data-dir=Users/<username>/Library/Application Support/Google/Chrome/Default")
options.add_argument("user-data-dir=/tmp/david2")
prefs = {'download.default_directory' : '/Users/dvas22/Desktop/David/www/geography/downloads'}
prefs = {'download.prompt_for_download' : False}
options.add_experimental_option('prefs', prefs)

service = Service()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


#Driver Type 2: 
'''
driver = webdriver.Chrome(service=svc, options=options)

options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")

#options.add_argument("user-data-dir=/tmp/david")
options.add_argument("user-data-dir=/tmp/david2")
#download_directory = /Users/dvas22/Downloads 
#download_directory = /Users/dvas22/Desktop/David/www/geography/downloads
 
#prefs = {'download.default_directory' : '/Users/dvas22/Desktop/David/www/geography/downloads'}
#prefs = {'download.default_directory' : '/Users/david/Desktop/David/www/geography/downloads/temp'}
prefs = {'download.prompt_for_download' : False}
#prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
#chrome_options.add_experimental_option("prefs",{'download.prompt_for_download': True})
options.add_experimental_option('prefs', prefs)
#options.add_experimental_option("detach", True)
svc = webdriver.ChromeService(executable_path=binary_path)
'''