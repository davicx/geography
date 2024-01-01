import time
from classes.UserClass import UserClass
from classes.BasinClass import BasinClass

currentUser = UserClass("aral", "david", True)
currentBasin = BasinClass("aral", True)

currentUser.getName()
paths = currentUser.getPath()

geography_folder = paths["geography_folder"]
download_folder_temp = paths["download_folder_temp"]
download_folder = paths["download_folder"]
status_file = paths["status_file"]

print(geography_folder)
print(download_folder_temp)
print(download_folder)
print(status_file)

search_link = currentBasin.get_basin_path()

print(search_link)