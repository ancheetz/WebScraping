import json
import pandas as pd

with open('/Users/aczarnecki/Documents/bcr/Git/PYTHON/WebScraping/ec2.json') as f:
    data = json.load(f)

print(data)

print(type(data))

data_info = [data]
data_df = pd.DataFrame(data_info)
data_df.to_csv('Data.csv')

