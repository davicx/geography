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
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--log-level=3')

# Provide the path of chromedriver present on your system.
driver = webdriver.Chrome(options=options, chromedriver_path=executable_path)
driver.get("https://www.example.com")

# Send a get request to the url
driver.get('https://www.geeksforgeeks.org/')
time.sleep(60)
driver.quit()
print("Done")

'''
import os
import pandas as pd
import time
options = Options()
#driver = webdriver.Chrome(options=options)
#chrome_driver = 'chromedriver'
#driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='114.0.5735.90').install()), options=options)
#driver = webdriver.Chrome(chrome_driver)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

print("Hello")
landing_page = "www.google.com"
time.sleep(2)
driver.get(landing_page)
time.sleep(2)

'''


#import HelloClass as hello


#options = Options()
#options.page_load_strategy = 'normal'
#options.add_argument("--start-maximized")
#options.add_argument("user-data-dir=/tmp/david")
#prefs = {'download.default_directory' : '/Users/dvas22/Desktop/David/www/geography/downloads'}
#options.add_experimental_option('prefs', prefs)

#116.0.5845.96
#116.0.5845.96
#driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='114.0.5735.90').install()), options=options)
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install('https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/mac-arm64/chromedriver-mac-arm64.zip')), options=options)
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install('https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/mac-arm64/chromedriver-mac-arm64.zip')), options=options)

#driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
#driver = webdriver.Chrome(executable_path='driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='114.0.5735.90').install()), options=options)')
#driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='114.0.5735.90').install()), options=options)
#pip install webdriver-managerdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


#driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='114.0.5735.90').install()), options=options)
