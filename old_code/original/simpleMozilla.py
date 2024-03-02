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

from selenium.webdriver.firefox.options import Options

import os
import pandas as pd
import time

options = Options()
#options.set_preference("browser.download.folderList", 2)
#options.set_preference("browser.download.manager.showWhenStarting", False)
#options.set_preference("browser.download.dir", "/Users/david/Desktop/David/www/geography/web_page/downloads")
#options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(options=options)

landing_page = "file:///Users/david/Desktop/David/www/geography/web_page/index.html"
driver.get(landing_page)
driver.maximize_window()
time.sleep(2)

#Download File
time.sleep(2)
click_element = driver.find_element(By.ID, "download")
time.sleep(1)  
click_element.click()
time.sleep(2)  
count = 2

#Send Text (Works)
count = 0
while count < 2:
    try:
        send_element = driver.find_element(By.ID, "text-id")
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




'''
    while download_wait < 10:
        try:
            #ResultsList_Aral_202207_1_60.ZIP
            print("File downloaded and moved to /Users/david/Desktop/David/www/geography/downloads/excel/", basin_code)

            original_path = "/Users/david/Desktop/David/www/geography/downloads/"
            fileNameOriginal = original_path + download_file_name + ".ZIP"

            final_path = "/Users/david/Desktop/David/www/geography/downloads/excel/"
            fileNameNew = final_path + basin_code + "/" + download_file_name + ".ZIP"

            os.rename(fileNameOriginal, fileNameNew)
            download_wait = 12
            time.sleep(5)

        except FileNotFoundError:
            print("The file has not finished downloading yet")
            download_wait = download_wait + 1
            time.sleep(5)
    '''




'''
from selenium.webdriver.firefox.options import Options

options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", "./downloads")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(options=options)


'''


'''
import pytest
from selenium import webdriver

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


@pytest.fixture(scope='session')
def driver(request):
    """Set up webdriver fixture."""
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(executable_path="firefox.geckodriver")
    driver = webdriver.Firefox(options=options, service=service)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()
'''