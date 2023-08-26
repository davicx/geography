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
options.add_argument("user-data-dir=/tmp/david")
prefs = {'download.default_directory' : '/Users/dvas22/Desktop/David/www/geography/downloads'}
options.add_experimental_option('prefs', prefs)



driver = webdriver.Chrome()

#driver.get("https://www.google.com/")

landing_page = "file:///Users/dvas22/Desktop/David/www/geography/test.html"
driver.get(landing_page)

print("hi")

time.sleep(60)


'''

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
options.add_argument("user-data-dir=/tmp/david")
prefs = {'download.default_directory' : '/Users/dvas22/Desktop/David/www/geography/downloads'}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome('Users/dvas22/Desktop/David/www/geography/drivers/chromedriver')








''' 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

from selenium import webdriver


driver = webdriver.Chrome('Users/dvas22/Desktop/David/www/geography/drivers/chromedriver')
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

'''

'''