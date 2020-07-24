import requests, re, json, csv, lxml
from bs4 import BeautifulSoup as bs

#search initial URL, then move onto individuals page links
URL = "https://en.wikipedia.org/wiki/List_of_countries_by_tea_consumption_per_capita"
response = requests.get(URL)

#print(response.status_code)
#print(response.text[:200])

page = (response.text)
soup = bs(page, 'lxml')

tea_nations= [s.text for s in soup.find_all('span', 'data-sort-value', class_='datasortkey')]
print(tea_nations)
