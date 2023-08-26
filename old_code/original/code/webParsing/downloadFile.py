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


def main():
    #download_files()
    move_file("my_name.ZIP", "/Users/david/Desktop/David/www/geography/web_page/downloads", "new_name.ZIP", "/Users/david/Desktop/David/www/geography/web_page/downloads/basin")
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

def move_file(fileNameOriginal, original_path, fileNameNew, final_path):
    current_file = original_path + "/" + fileNameOriginal
    moved_file = final_path + "/" + fileNameNew


    #Step 1: Check if File was downloaded
    if os.path.isfile(current_file):
        print("File was found")
        os.rename(current_file, moved_file)
    else: 
        print("FIle not foound")

    #Step 2: Move to new location

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




if __name__ == "__main__":
    main()