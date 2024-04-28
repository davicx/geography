

#APPENDIX
#SIMPLE Windows:

'''
options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")

options.add_argument(data_dir_mm)
prefs = {'download.default_directory' : default_download_mm}
options.add_experimental_option('prefs', prefs)

service = Service()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com/")

print(driver.title)
time.sleep(30)
'''



#PATHS: 
'''
data_dir = "user-data-dir=Users/username/Library/Application Support/Google/Chrome/Default"
default_download = "/Users/dvas22/Desktop/David/www/geography/downloads"

options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")

options.add_argument(data_dir)
prefs = {'download.default_directory' : default_download}
options.add_experimental_option('prefs', prefs)

service = Service()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com/")

print(driver.title)
time.sleep(30)

'''

#SIMPLE Windows:
#Microsoft Example: 
'''
options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")
data_dir_mm = "user-data-dir=C://Users/Melissa/Library/Application Support/Google/Chrome/Default"
default_download_mm = "/Users/dvas22/Desktop/David/www/geography/downloads"
options.add_argument(data_dir_mm)
prefs = {'download.default_directory' : default_download_mm}
options.add_experimental_option('prefs', prefs)

service = Service()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com/")

print(driver.title)
time.sleep(30)
'''

#EXAMPLE 3 (Doesnt work?)
'''
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
