import os
import time



def move_rename_file(original_file_name, original_file_path, new_file_name, new_file_path):
    download_wait_count = 0
    total_wait_seconds = 0
    #/Users/dvas22/Downloads/ResultsList_Aral_202207_1_220.ZIP
    
    while download_wait_count < 20:
        try:
            original_file_full = original_file_path + original_file_name
            new_file_full = new_file_path + new_file_name + ".pdf"

            print("original_file_full")
            print(original_file_full)
            print("new_file_full")
            print(new_file_full)
            #print("ResultsList_Aral_202207_1_220")

            os.rename(original_file_full, new_file_full)
            print("The file was sucesfully moved")
            download_wait_count = 20
            time.sleep(5)
            return True

        except FileNotFoundError:
            download_wait_count = download_wait_count + 1
            total_wait_seconds = total_wait_seconds + 1
            print("The file has not finished downloading yet pausing to sleep")
            print("Total Wait ", total_wait_seconds * 5)

    #Return true if the files were downloaded and moved 
    if download_wait_count < 20:
        return True
    else:
        return False

base_path_prefix = "/Users/david/"
base_path = base_path_prefix + "Desktop/David/www/geography/"

download_folder_temp = base_path_prefix + "Downloads/"
download_folder = base_path + "downloads/aral/excel/"
download_folder_pdf = base_path + "downloads/aral/pdf/"
original_file_name = "Files (100).PDF"
download_file_name = "ResultsList_" + "aral" + "_202207_" + "min" + "_" + "max" + "_PDF"


move_rename_file(original_file_name, download_folder_temp, download_file_name, download_folder_pdf)
