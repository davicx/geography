import pandas as pd

#basin_code = "tigr"
#now I just need to figure out how to get this to link with main.py variable
#where does userclass or other basinclass talk to main.py?


class SearchBasinClass:
    def __init__(self, basin_code, search_term):
#    def __init__(self, basin, search_term):
        self.basin = basin_code
        self.search_term = self.get_search_term()
#        self.external_user = external_user

    def get_search_term(self):
        try:
            # change the file path to that of the downloaded edited tracking sheet
            df = pd.read_excel('/Users/selenawallace/Documents/Data_Science/TrackingSheet_basinterms.xlsx')

            # Find the row corresponding to the provided code
            row = df[df['BCODE'] == self.basin_code.upper()]
            
            # Check if the row exists
            if not row.empty:
                # Retrieve the search term from the DataFrame
                #note that I had to change the column title in excel for this to work
                #search_term = row['Basin_Specific_Terms'].values[0] #copied from test
                return row['Basin_Specific_Terms'].values[0]
            else:
                print(f"No search term found for code: {self.code}")
                return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


'''
# Example usage:
code = basin_code
my_object = MyClass(code)
if my_object.search_term is not None:
    print(f"Search term for {code}: {my_object.search_term}")
else:
    print("Failed to retrieve search term.")



    def get_basin_path(self):
        if self.basin.lower() == "tigr":
#            if self.external_user == True:
#                search_link = ""
#            else:
            search_link = ""
            return search_link
        
        elif self.basin.lower() == "CLDO":
            
            #External user here
            if self.external_user == True:
                search_link = ""
            
            #Tufts user here
            else:
                search_link =  ""
            
            return search_link
        
        elif self.basin.lower() == "DURO":
            if self.external_user == True:
                search_link = ""
            else:
                search_link = ""
            return search_link
        
        elif self.basin.lower() == "FRSR":
            if self.external_user == True:
                search_link = ""
            else:
                search_link = ""
            return search_link
                
        elif self.basin.lower() == "GANG":
            if self.external_user == True:
                search_link = ""
            else:
                search_link = ""
            return search_link
                
        elif self.basin.lower() == "LPTA":
            if self.external_user == True:
                search_link = ""
            else:
                search_link = ""
            return search_link
                
        elif self.basin.lower() == "MEKO":
            if self.external_user == True:
                search_link = ""
            else:
                search_link = ""
            return search_link
                
        elif self.basin.lower() == "BCODE":
            if self.external_user == True:
                search_link = ""
            else:
                search_link = ""
            return search_link
                
        elif self.basin.lower() == "MISS":
            if self.external_user == True:
                search_link = ""
            else:
                search_link = ""
            return search_link
                
        elif self.basin.lower() == "NELS":
            if self.external_user == True:
                search_link = ""
            else:
                search_link = ""
            return search_link
                
        elif self.basin.lower() == "NILE":
            if self.external_user == True:
                search_link = ""
            else:
                search_link = ""
            return search_link
                
        elif self.basin.lower() == "ORAN":
            if self.external_user == True:
                search_link = ""
            else:
                search_link = ""
            return search_link
                
        elif self.basin.lower() == "ORIN":
            if self.external_user == True:
                search_link = ""
            else:
                search_link = ""
            return search_link
                
        elif self.basin.lower() == "POXX":
            if self.external_user == True:
                search_link = ""
            else:
                search_link = ""
            return search_link
        
                
        elif self.basin.lower() == "ZAMB":
            if self.external_user == True:
                search_link = ""
            else:
                search_link = ""
            return search_link
 '''