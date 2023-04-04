from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time

options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")
options.add_argument("user-data-dir=/tmp/david")

PATH = "/Users/david/Desktop/David/www/development/geography/chromedriver.exe"
#driver = webdriver.Chrome(options=options)
#browser = webdriver.Chrome(chrome_path, chrome_options=options)
driver = webdriver.Chrome(PATH, options=options)

#Login 
driver.get("https://library.oregonstate.edu/")
time.sleep(3)
element = driver.find_element(By.ID,"term-1search")
element.send_keys("nexis uni")
element.send_keys(Keys.RETURN)

time.sleep(120)