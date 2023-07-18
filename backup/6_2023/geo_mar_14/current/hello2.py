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

driver.get("https://library.oregonstate.edu/")
time.sleep(3)
element = driver.find_element(By.ID,"term-1search")
element.send_keys("nexis uni")
element.send_keys(Keys.RETURN)
time.sleep(12)
driver.find_element(By.CSS_SELECTOR, "#SEARCH_RESULT_RECORDID_alma99492178701865 mark").click()
time.sleep(8)
driver.find_element(By.CSS_SELECTOR, ".item-title:nth-child(1)").click()
time.sleep(12)

driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.CSS_SELECTOR, ".advanced-search").click()
time.sleep(15)

#Navigate to the first level search and move to this new tab 
#this link does not have the second search 
#linkSearch = "https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=2169ffa2-7782-4990-ab46-cc5633131f4b&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(box1)+and+hlead(box2)+and+not+hlead(box3)&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=12%2F08%2F2000to12%2F08%2F2022%7Cdatebetween&pdfromadvancedsearchpage=true&ecomp=3xLg9kk&earg=pdpsf&prid=ed3fc566-6534-4898-8343-4763b6de7c5f"

#This link might have it 
linkSearch = "https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=a4370a98-a1cc-469d-b871-38af4134db42&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(box1)+and+hlead(box2)+and+not+hlead(box3)&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=12%2F08%2F2000to12%2F08%2F2022%7Cdatebetween&pdfromadvancedsearchpage=true&ecomp=3xLg9kk&earg=pdpsf&prid=ed3fc566-6534-4898-8343-4763b6de7c5f"
driver.get(linkSearch)
time.sleep(10)

#Turn duplicates on 
driver.find_element(By.CSS_SELECTOR, ".custom-control-indicator").click()

time.sleep(12)

driver.find_element(By.CSS_SELECTOR, ".has_tooltip:nth-child(1) > .la-Download").click()
time.sleep(12)
driver.find_element(By.ID, "SelectedRange").click()
driver.find_element(By.ID, "SelectedRange").send_keys("1-10")
time.sleep(2)
driver.find_element(By.ID, "FileName").click()
driver.find_element(By.ID, "FileName").send_keys("myname")
time.sleep(12)
driver.find_element(By.CSS_SELECTOR, ".button-group > .primary").click()
time.sleep(120)
