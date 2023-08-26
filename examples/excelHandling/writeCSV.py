# importing pandas as pd
import pandas as pd

name = ["david", "davey"]
location = ["corvallis", "corvallis"]

# dictionary of lists
names = {'name': name, 'location': location}
     
df = pd.DataFrame(names)
 
print(df)
df.to_csv('names.csv')