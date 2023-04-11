# importing pandas as pd
import pandas as pd
 
# list of name, degree, score
name = ["david", "frodo"]
location = ["shire", "Shire"]
scr = [90, 40, 80, 98]
 
# dictionary of lists
shire = {'name': name, 'location': location}
     
df = pd.DataFrame(shire)
 
print(df)
df.to_csv('file1.csv')