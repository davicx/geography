import os
import time


#download_file_name = "ResultsList_" + basin_code + "_202207_" + min + "_" + max
original_file_path = "/Users/dvas22/Desktop/David/www/geography/examples/fileHandling/fileOriginalLocation/"
new_file_path = "/Users/dvas22/Desktop/David/www/geography/examples/fileHandling/fileNewLocation/"

try:
    original_file_location = original_file_path + "pdf_name.PDF"
    new_file_location = new_file_path + "pdf_new_name.PDF"

    os.rename(original_file_location, new_file_location)
    time.sleep(5)

except FileNotFoundError:
    print("The file has not finished downloading yet")
    time.sleep(5)
