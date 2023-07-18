from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import pandas as pd
import time

logged_in = True

def main():
    if logged_in == False:
        login_user()
    else:   
        first_level_search()
        second_level_search()
        download_results()
 
def login_user():
    print("Opening login screen, please login with Duo")
    
def first_level_search():
    print("STEP 1: First Level Search") 
    data = pd.read_csv('data/firstLevelSearch.csv')

    for index, row in data.iterrows():
        field_one_search_terms = row['field_one'].replace(" ", "+")
        field_two_search_terms = row['field_two'].replace(" ", "+")
        field_three_search_terms = row['field_three'].replace(" ", "+")

    print(field_one_search_terms)
    print("")
    print(field_two_search_terms)
    print("")
    print(field_three_search_terms)
    first_search_url = "https://advance-lexis-com.oregonstate.idm.oclc.org/search/?pdmfid=1516831&crid=c753d4b1-4bcb-4d62-bc2b-e5488b2cca1d&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(" + field_one_search_terms + ")+and+hlead(" + field_two_search_terms + ")+and+not+hlead(" + field_three_search_terms + ")&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=06%2F30%2F2008to01%2F10%2F2023%7Cdatebetween&pdfromadvancedsearchpage=true&ecomp=3xLg9kk&earg=pdpsf&prid=3c1ebaf8-b772-4481-a033-9d93018ce1b8"
    #print(first_search_url)


def second_level_search():							
    print("Second Level")
    dataSecondLevel = pd.read_csv('data/secondLevelSearch.csv')

    for index, row in dataSecondLevel.iterrows():
        basin_count = row['basin_count']
        search_type = row['search_type']
        search_terms = row['search_terms'].replace(" ", "+")
        basin_code = row['basin_code']
        basin_name = row['basin_name']
        ra_name = row['ra_name']
        search_completed = row['search_completed']
        preliminary_search = row['preliminary_search']
        notes = row['notes']
        print("BASIN NAME " + basin_name)
        print(search_terms)
        print("")

def download_results():
    print("Download results") 


if __name__ == "__main__":
    main()
