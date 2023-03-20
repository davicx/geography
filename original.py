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

#PATH = "/Users/david/Desktop/David/www/development/geography/chromedriver.exe"
PATH = "/Users/david/Desktop/David/www/geography/drivers/chromedriver.exe"
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
time.sleep(15)

driver.switch_to.window(driver.window_handles[1])
time.sleep(15)

driver.find_element(By.CSS_SELECTOR, ".advanced-search").click()
time.sleep(15)

#Navigate to the first level search and move to this new tab 
boxOne = "*water* OR river* OR lake OR dam OR stream OR tributary OR diversion OR irrigation OR pollution OR water quality OR flood! OR drought! OR channel OR canal OR hydroelect! OR   OR groundwater OR aquifer OR drought OR recharge OR water table OR bore hole"
boxTwo = "treaty OR agree! OR negotiat! OR resolution OR commission OR secretariat OR joint management OR basin management OR peace OR accord OR peace accord OR settle! OR cooperat! OR collaborat! OR disput! OR conflict! OR disagree! OR sanction! OR war OR troops OR letter of protest OR hostility OR shots fired OR boycott OR protest! OR appeal OR intent OR reject OR threat! OR force OR coerce OR assault OR fight OR demand OR disapprove OR diploma! OR statement OR memorandum"
boxThree = "ocean OR navigat! OR nuclear OR water cannon OR light water reactor OR mineral water OR hold water OR cold water OR hot water OR water canister OR water tight OR water down OR flood of refugees OR Rivera OR Suez OR Panama OR oil OR drugs OR three gorges OR waterski OR watermelon OR dishwater OR waterproof OR water resistant OR water bath"
searchLink = "https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=1c45062b-b31a-4c69-ac7d-2d5c3c7c33b5&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(box1)+and+hlead(box2)+and+not+hlead(box3)&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=12%2F08%2F2000to12%2F08%2F2022%7Cdatebetween&pdfromadvancedsearchpage=true&ecomp=3xLg9kk&earg=pdpsf&prid=ed3fc566-6534-4898-8343-4763b6de7c5f"
#searchLink = "https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=1c45062b-b31a-4c69-ac7d-2d5c3c7c33b5&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(stream)+and+hlead(water)+and+not+hlead(Panama)&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=12%2F08%2F2000to12%2F08%2F2022%7Cdatebetween&pdfromadvancedsearchpage=true&ecomp=3xLg9kk&earg=pdpsf&prid=ed3fc566-6534-4898-8343-4763b6de7c5f"

driver.get(searchLink)
time.sleep(12)

#Turn duplicates on 
driver.find_element(By.CSS_SELECTOR, ".custom-control-indicator").click()

time.sleep(5)
driver.execute_script("window.scrollTo(0,103)")
time.sleep(12)
#second Level Search 
#secondSearchTerm = "IB_FDDBasinNames"
secondSearchTerm = "box1"
driver.find_element(By.ID, "zz2yk_search").click()
driver.find_element(By.ID, "zz2yk_search").send_keys(secondSearchTerm)

#driver.find_element(By.ID, "zz2yk_search").click()
#driver.find_element(By.ID, "zz2yk_search").send_keys("startsearchwithinresults")
time.sleep(12)

driver.find_element(By.CSS_SELECTOR, ".src-submit").click()

time.sleep(12)

driver.find_element(By.CSS_SELECTOR, ".custom-control-indicator").click()
#driver.execute_script("window.scrollTo(0,101)")
#driver.find_element(By.ID, "zznyk_search").click()
#driver.find_element(By.ID, "zznyk_search").send_keys("adige")
#driver.find_element(By.ID, "podfiltersbuttonsearch").click()
#driver.find_element(By.ID, "podfiltersbuttonsearch").click()
#driver.find_element(By.ID, "zznyk_search").click()
#driver.find_element(By.CSS_SELECTOR, ".src-submit").click()
#driver.execute_script("window.scrollTo(0,0)")
time.sleep(12)
driver.find_element(By.CSS_SELECTOR, ".has_tooltip:nth-child(1) > .la-Download").click()
time.sleep(12)
driver.find_element(By.CSS_SELECTOR, ".DeliveryItemType > .row:nth-child(3) > label").click()
time.sleep(8)
driver.find_element(By.CSS_SELECTOR, ".nested:nth-child(3) #SelectedRange").click()
time.sleep(8)
driver.find_element(By.CSS_SELECTOR, ".nested:nth-child(3) #SelectedRange").send_keys("1-10")
driver.find_element(By.CSS_SELECTOR, ".Format > .row:nth-child(4)").click()
time.sleep(2)
driver.find_element(By.ID, "FileName").click()
time.sleep(2)
driver.find_element(By.ID, "FileName").send_keys("put the file name here")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".button-group > .primary").click()

#DONT WORK MAYBE?
'''
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
'''
