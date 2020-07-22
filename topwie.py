import requests, re, json
import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup as bs

URL = "https://en.wikipedia.org/wiki/Top_50_Influential_Women_in_Engineering"
response = requests.get(URL)

#print(response.status_code)
#print(response.text[:200])

page= response.text
soup= bs(page, 'lxml')

#scrape name of winners for 2016
winners= [winner.text for winner in soup.find_all('ul')[1].find_all('a')]
win_2016 = (json.dumps(winners, indent=4))
#print(win_2016)

#scrape degrees for each winner for 2016
degrees= [degree.text for degree in soup.find_all('ul')[1].find_all('li')]
deg_2016= (json.dumps(degrees, indent=4))
#print(degrees)

#scrape name of winners for 2017
winner_2017=[w.text for w in soup.find_all('ul')[2].find_all('li')]
win_2017= (json.dumps(winner_2017, indent=4))
#print(win_2017)

#degree for 2017 winner
degree_2017=[d.text for d in soup.find_all('ul')[2].find_all('li')]
deg_2017= (json.dumps(degree_2017, indent=4))
#print(deg_2017)

top_2016_dict= degrees 
print(top_2016_dict)

top_2017_dict= degree_2017
print(top_2017_dict)

top_2016_info = [top_2016_dict]
top_2016_df = pd.DataFrame(top_2016_info)
top_2016_df.to_csv('Top_2016.csv')

top_2017_info = [top_2017_dict]
top_2017_df = pd.DataFrame(top_2017_info)
top_2017_df.to_csv('Top_2017.csv')