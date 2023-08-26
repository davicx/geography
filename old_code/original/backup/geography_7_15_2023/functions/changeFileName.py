import os
path = "/Users/david/Desktop/David/www/geography/downloads/"
fileName = "Files (100).PDF"
newFileName = "hi.PDF"
fileBegin = path + fileName
fileNew= path + newFileName
os.rename(fileBegin, fileNew)