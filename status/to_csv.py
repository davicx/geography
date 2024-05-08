import os
import pandas as pd

# Directory containing XLSX files (CHANGE to pdf folder if needed)
xlsx_directory = '/Users/selenawallace/Documents/Data_Science/geography/status/excel/fromBox/'

# Output directory for CSV files
output_directory = '/Users/selenawallace/Documents/Data_Science/geography/status/excel/'

# List all files in the directory
files = os.listdir(xlsx_directory)

# Iterate over each file
for file in files:
    if file.endswith('.xlsx'):
        # Construct input and output file paths
        input_file = os.path.join(xlsx_directory, file)
        filename, _ = os.path.splitext(file)
        output_file = os.path.join(output_directory, filename.lower().replace('_excel', '') + '.csv')
        
        # Read the XLSX file
        df = pd.read_excel(input_file)
        
        # Write to CSV
        df.to_csv(output_file, index=False, date_format='%m/%d/%Y')

print("Conversion completed successfully.")
