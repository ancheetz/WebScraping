import requests, re, json, csv
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

#create dictionary of 2016; add 2016 as default value for each
top_2016_dict = {year: "2016" for year in degrees}
print(top_2016_dict)
#create csv file for dictionary
with open("Top_Eng_16.csv", 'w') as f:
    for key in top_2016_dict.keys():
        f.write("%s, %s\n" % (key, top_2016_dict[key]))

#create dictionary of 2017; add 2017 as default value for each 
top_2017_dict = {year: "2017" for year in degree_2017}
print(top_2017_dict)
#create csv file for dictionary
with open("Top_Eng_17.csv", 'w') as fl:
    for key in top_2017_dict.keys():
        fl.write("%s, %s\n" % (key, top_2017_dict[key]))
