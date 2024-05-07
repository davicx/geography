import os
import zipfile
import pandas as pd

#put in bcode
BCODE = 'bakr'

def extract_zip(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(zip_folder)

# Path to the folder containing the zip files
zip_folder_base = '/Users/selenawallace/Documents/Data_Science/geography/downloads/'
zip_folder = zip_folder_base + BCODE + '/excel'

# Path to the folder where you want to save the combined Excel file
output_folder = zip_folder #I can ask where they want it

# Get a list of all zip files in the zip_folder
zip_files = [os.path.join(zip_folder, file) for file in os.listdir(zip_folder) if file.endswith('.ZIP')]

# Extract all zip files in the zip_folder
for zip_file in zip_files:
    print(f"Extracting {zip_file}...")
    extract_zip(zip_file)
    print(f"{zip_file} extracted successfully.")

# Print the list of files in the directory after extraction
print("Files in directory after extraction:")
print(os.listdir(zip_folder))

# Get a list of all extracted Excel files
excel_files = [file for file in os.listdir(zip_folder) if file.endswith('.xlsx')]

# Combine all Excel files into one DataFrame
combined_df = pd.concat([pd.read_excel(os.path.join(zip_folder, file)) for file in excel_files])

# Write the combined DataFrame to a new Excel file
file_name = BCODE + '_excel_downloadresults.xlsx'
output_file = os.path.join(output_folder, file_name)
combined_df.to_excel(output_file, index=False)
        # Write the combined DataFrame to a new Excel file

print(f'Combined file saved at {output_file}')
