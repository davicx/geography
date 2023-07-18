# importing pandas as pd
import pandas as pd
 
# list of name, degree, score
name = ["david", "frodo"]
location = ["shire", "Shire"]

# dictionary of lists
shire = {'name': name, 'location': location}
     
df = pd.DataFrame(shire)
 
print(df)
df.to_csv('names.csv')