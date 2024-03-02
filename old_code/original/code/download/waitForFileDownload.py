
import os
import time


path = "/Users/david/Desktop/David/www/geography/images/"
fileWait = 0

while fileWait < 5:
    try:
        fileNameOriginal = path + "tumblr.PNG"
        fileNameNew = path + "hi" + "tumblr.PNG"
        os.rename(fileNameOriginal, fileNameNew)
        time.sleep(5)
    except FileNotFoundError:
        print("The file has not finished downloading yet")
        fileWait = fileWait + 1
        time.sleep(5)

