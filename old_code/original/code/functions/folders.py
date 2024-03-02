import os 

newpath = '/Users/david/Desktop/David/www/geography/downloads/new' 
if not os.path.exists(newpath):
    os.makedirs(newpath)