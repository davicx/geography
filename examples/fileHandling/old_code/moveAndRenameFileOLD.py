import os
import time

download_wait = 0

basin_code = "Aral"
min = str(1)
max = str(60)

#folder fileOriginalLocation
#folder fileNewLocation

download_file_name = "ResultsList_" + basin_code + "_202207_" + min + "_" + max

while download_wait < 10:
    try:
        #ResultsList_Aral_202207_1_60.ZIP
        print("File downloaded and moved to /Users/david/Desktop/David/www/geography/downloads/excel/", basin_code)
        original_path = "/Users/david/Desktop/David/www/geography/downloads/"
        fileNameOriginal = original_path + download_file_name + ".ZIP"

        final_path = "/Users/david/Desktop/David/www/geography/downloads/excel/"
        fileNameNew = final_path + basin_code + "/" + download_file_name + ".ZIP"
        os.rename(fileNameOriginal, fileNameNew)
        download_wait = 12
        time.sleep(5)

    except FileNotFoundError:
        print("The file has not finished downloading yet")
        download_wait = download_wait + 1
        time.sleep(5)
