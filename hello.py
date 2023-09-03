from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import time

options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")

options.add_argument("user-data-dir=Users/<username>/Library/Application Support/Google/Chrome/Default")
prefs = {'download.default_directory' : '/Users/dvas22/Desktop/David/www/geography/downloads'}
options.add_experimental_option('prefs', prefs)

service = Service()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://advance-lexis-com.ezproxy.library.tufts.edu/practice/?pdmfid=1516831&crid=b9ff301d-2c5b-415b-9c45-94c6cc6dc472&config=00JAAzNzdlNTFkNS00MDk2LTQzMTItYWM4Mi1kZjM0NGVlNDNkNzEKAFBvZENhdGFsb2eMH3E8B5wUwBgbm9pcVO5K&ecomp=ybJgkgk&prid=4f1f54e8-ca88-46d3-8193-9642eb75d530")
#driver.get("https://www.python.org")

time.sleep(20)
driver.get("https://advance-lexis-com.ezproxy.library.tufts.edu/practice/?pdmfid=1516831&crid=b9ff301d-2c5b-415b-9c45-94c6cc6dc472&config=00JAAzNzdlNTFkNS00MDk2LTQzMTItYWM4Mi1kZjM0NGVlNDNkNzEKAFBvZENhdGFsb2eMH3E8B5wUwBgbm9pcVO5K&ecomp=ybJgkgk&prid=4f1f54e8-ca88-46d3-8193-9642eb75d530")
print(driver.title)


time.sleep(30)