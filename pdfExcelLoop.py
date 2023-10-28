import pandas as pd
import time

'''
#FILE PATHS
#Base Path
base_path_prefix = "/Users/dvas22/"
#base_path_prefix = "/Users/david/"

#Main 
base_path = base_path_prefix + "Desktop/David/www/geography/"

#Download Folder
download_folder_temp = base_path_prefix + "Downloads/"
download_folder = base_path + "downloads/aral/excel/"
download_folder_pdf = base_path + "downloads/aral/pdf/"

#Search Link
if external_user == True:
    search_link = "https://advance-lexis-com.ezproxy.library.tufts.edu/search/?pdmfid=1516831&crid=8346dc40-81b7-47ac-9469-cb518c95d880&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(*water*+OR+river*+OR+lake+OR+dam+OR+stream+OR+tributary+OR+diversion+OR+irrigation+OR+pollution+OR+water+quality+OR+flood!+OR+drought!+OR+channel+OR+canal+OR+hydroelect!+OR+reservoir+OR+groundwater+OR+aquifer+OR+drought+OR+recharge+OR+%22water+table%22+OR+%22bore+hole%22)+and+hlead(treaty+OR+agree!+OR+negotiat!+OR+resolution+OR+commission+OR+secretariat+OR+joint+management+OR+basin+management+OR+peace+OR+accord+OR+%22peace+accord%22+OR+settle!+OR+cooperat!+OR+collaborat!+OR+disput!+OR+conflict!+OR+disagree!+OR+sanction!+OR+war+OR+troops+OR+%22letter+of+protest%22+OR+hostility+OR+%22shots+fired%22+OR+boycott+OR+protest!+OR+appeal+OR+intent+OR+reject+OR+threat!+OR+force+OR+coerce+OR+assault+OR+fight+OR+demand+OR+disapprove+OR+diploma!+OR+statement+OR+memorandum)+and+hlead(Aral+OR+Syr+Daria+OR+Naryn+OR+Amu+Daria+OR+Syr+Darya+OR+Amu+Darya+OR+Akhangaran+OR+Chirchik)+and+not+hlead(ocean+OR+navigat!+OR+nuclear+OR+%22water+cannon%22+OR+%22light+water+reactor%22+OR+%22mineral+water%22+OR+%22hold+water%22+OR+%22cold+water%22+OR+%22hot+water%22+OR+%22water+canister%22+OR+%22water+tight%22+OR+%22+water+down%22+OR+%22flood+of+refugees%22+OR+Rivera+OR+Suez+OR+Panama+OR+oil+OR+drugs+OR+%22three+gorges%22+OR+waterski+OR+watermelon+OR+dishwater+OR+waterproof+OR+%22water+resistant%22+OR+%22water+bath%22)&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=undefined%7Calldates&pdfromadvancedsearchpage=true&ecomp=yxLg9kk&earg=pdpsf&prid=c0d34a78-a8aa-4c9b-8ad0-d00c56ca39bd"
else:
    search_link =  "https://advance-lexis-com.ezproxy.library.tufts.edu/search/?pdmfid=1516831&crid=928f5e0f-556b-4f46-bf5d-1c43de32c3f8&pdpsf=&pdpost=&pdstartin=urn%3Ahlct%3A16&pdsearchterms=hlead(*water*+OR+river*+OR+lake+OR+dam+OR+stream+OR+tributary+OR+diversion+OR+irrigation+OR+pollution+OR+water+quality+OR+flood!+OR+drought!+OR+channel+OR+canal+OR+hydroelect!+OR+reservoir+OR+groundwater+OR+aquifer+OR+drought+OR+recharge+OR+%22water+table%22+OR+%22bore+hole%22)+and+hlead(treaty+OR+agree!+OR+negotiat!+OR+resolution+OR+commission+OR+secretariat+OR+joint+management+OR+basin+management+OR+peace+OR+accord+OR+%22peace+accord%22+OR+settle!+OR+cooperat!+OR+collaborat!+OR+disput!+OR+conflict!+OR+disagree!+OR+sanction!+OR+war+OR+troops+OR+%22letter+of+protest%22+OR+hostility+OR+%22shots+fired%22+OR+boycott+OR+protest!+OR+appeal+OR+intent+OR+reject+OR+threat!+OR+force+OR+coerce+OR+assault+OR+fight+OR+demand+OR+disapprove+OR+diploma!+OR+statement+OR+memorandum)+and+hlead(Aral+OR+Syr+Daria+OR+Naryn+OR+Amu+Daria+OR+Syr+Darya+OR+Amu+Darya+OR+Akhangaran+OR+Chirchik)+and+not+hlead(ocean+OR+navigat!+OR+nuclear+OR+%22water+cannon%22+OR+%22light+water+reactor%22+OR+%22mineral+water%22+OR+%22hold+water%22+OR+%22cold+water%22+OR+%22hot+water%22+OR+%22water+canister%22+OR+%22water+tight%22+OR+%22+water+down%22+OR+%22flood+of+refugees%22+OR+Rivera+OR+Suez+OR+Panama+OR+oil+OR+drugs+OR+%22three+gorges%22+OR+waterski+OR+watermelon+OR+dishwater+OR+waterproof+OR+%22water+resistant%22+OR+%22water+bath%22)&pdsearchtype=SearchBox&pdtypeofsearch=searchboxclick&pdsf=&pdquerytemplateid=&pdtimeline=undefined%7Calldates&pdfromadvancedsearchpage=true&ecomp=yxLg9kk&earg=pdpsf&prid=0b27b868-b378-4485-8a1f-7dd4553471f9"


    
def single_basin_search():
  for index, row in status_data_date.iterrows():
        basin = row['basin']
        key = row['key']
        start_date = row['start_date']
        end_date = row['end_date']
        finished = row['finished']

def download_pdf_bulk(index, basin_code, key, result_count_raw):
    print("LEVEL 1: download_pdf_bulk")
    #download_pdf(min_raw, max_raw)
    print(index, key, basin_code, result_count_raw)

#loop over 1 to 100 out function true if all pdf for that year range worked
def download_pdf(key, min_raw, max_raw):
    '''

#data = pd.read_csv('/Users/david/Desktop/David/www/geography/code/excelHandling/excel/updateExcel.csv', index_col=0)
data = pd.read_csv('/Users/dvas22/Desktop/David/www/geography/status/pdf/aral.csv', index_col=0)


def main():
    print("main")
    statusLoop()

def statusLoop():    
    for index, row in data.iterrows():
        basin = row['basin']
        key = row['key']
        set_date = row['set_date']
        start_date = row['start_date']
        end_date = row['end_date']
        start_count = row['start_count']
        stop_count = row['stop_count']
        total_count = row['total_count']
        finished = row['finished']


        #Run Search if it is not already Done
        if finished != 1:
            print("Run for ", basin, " key ", key, " set_date", set_date + " start_date", start_date, " end_date",  end_date)
        else:     
            print("The basin ", basin, " from ", start_date, " to ", end_date, " is already done so we are skipping")
            time.sleep(1)
'''


def download_file(index, start_count,stop_count,basin_count):
    print("Download from ", start_count, " to ", stop_count)
    write_status(index, basin_count)

            if stop_count < basin_count:
                download_file(index, start_count,stop_count,basin_count)
                time.sleep(1)
            else:
                mark_done(index)
                time.sleep(1)

def write_status(index, basin_count):
    data.loc[index, ['finished']] = [1]
    data.loc[index, ['total_count']] = [basin_count]
    df = pd.DataFrame(data)  
    df.to_csv('/Users/dvas22/Desktop/David/www/geography/examples/excelHandling/excel/updateNewExcel.csv')

def mark_done(index):
    data.loc[index, ['finished']] = [1]
    df = pd.DataFrame(data)  
    df.to_csv('/Users/dvas22/Desktop/David/www/geography/examples/excelHandling/excel/updateNewExcel.csv')

if __name__ == "__main__":
    main()  



def run_search(index):
    data.loc[index, ['finished']] = [1] 
    writeStatus()

def writeStatus(): 
    print("The data was downloaded marking complete")
    df = pd.DataFrame(data)  
    #df.to_csv('/Users/david/Desktop/David/www/geography/code/excelHandling/excel/updateExcel.csv')
    df.to_csv('/Users/dvas22/Desktop/David/www/geography/examples/excelHandling/updateExcel.py')








error = False
error = True
    if error == True:
        break 

import pandas as pd
import time


#Read Data in 
data = pd.read_csv('data/basinToDo.csv', index_col=0)

for index, row in data.iterrows():
    error = False
    basin = row['basin']
    start = row['start']
    stop = row['stop']
    finished = row['finished']
    print(basin)
    print(start, stop)
    print(finished)
    print("")
    data.loc[index, ['finished']] = ["True"]
    
    if index == 2: 
        data.loc[index, ['finished']] = ["Location2"]
        error = True

    if error == True:
        break 
    
    time.sleep(1)


df = pd.DataFrame(data)

print(df)
df.to_csv('data/basinToDo.csv')
'''