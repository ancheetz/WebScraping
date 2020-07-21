import requests, re, dateutil.parser
from bs4 import BeautifulSoup as bs

URL = "https://en.wikipedia.org/wiki/Top_50_Influential_Women_in_Engineering"
response = requests.get(URL)

#print(response.status_code)
#print(response.text[:200])

page= response.text
soup= bs(page)

#scrape name of winners for 2016
winners=soup.find_all('ul')[1].find_all('a')
#print only names of winners
def winner():
    for winner in winners:
        print(winner.text)

#scrape degrees for each winner for 2016
degrees=soup.find_all('ul')[1].find_all('li')
#print degree of each winner
def degree():
    for deg in degrees:
        print(deg.contents)

winner()
degree()

#scrape name of winners for 2017
winner_2017=soup.find_all('ul')[2].find_all('b')
#print each
for w17 in winner_2017:
    print(w17.text)

#degree for 2017 winner
deg_2017=soup.find_all('ul')[2].find_all('li')

for d17 in deg_2017:
   print(d17.contents)
