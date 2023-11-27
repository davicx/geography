from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path # this will get you the path variable

import time

#EXAMPLE 3
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path # this will get you the path variable
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")

options.add_argument("user-data-dir=Users/<username>/Library/Application Support/Google/Chrome/Default")
prefs = {'download.default_directory' : '/Users/dvas22/Desktop/David/www/geography/downloads'}
options.add_experimental_option('prefs', prefs)

svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc, options=options)
driver.get("https://www.google.com/")
time.sleep(60)
'''

#EXAMPLE 1: 
'''
options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")

options.add_argument("user-data-dir=Users/<username>/Library/Application Support/Google/Chrome/Default")
prefs = {'download.default_directory' : '/Users/dvas22/Desktop/David/www/geography/downloads'}
options.add_experimental_option('prefs', prefs)


svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc, options=options)
driver.get("https://www.google.com/")
'''

#EXAMPLE 2: 
options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")

options.add_argument("user-data-dir=Users/<username>/Library/Application Support/Google/Chrome/Default")
prefs = {'download.default_directory' : '/Users/dvas22/Desktop/David/www/geography/downloads'}
options.add_experimental_option('prefs', prefs)

service = Service()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com/")

time.sleep(20)
driver.get("https://www.google.com/")
print(driver.title)


time.sleep(30)