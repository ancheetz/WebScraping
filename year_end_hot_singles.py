import requests, csv, re, time
import numpy as np
from bs4 import BeautifulSoup as bs

URL = "https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2019"
response = requests.get(URL)

page = (response.text)
soup = bs(page, 'html.parser')

#Collect each row of data for our songs
full_list = soup.find_all('tr')
full_list = full_list[1:101]

def Year_End_Singles(full_list, csvwriter):
#Loop through all data
    for list in full_list:
        
        #Song number
        num = list.th.text.strip()

        #Song title
        all_titles = ([t.text for t in list.find_all('a')])[0]

        #Song href
        all_links = [a.get('href') for a in list.find_all('a', attrs={'href': re.compile("^/wiki/")})][0]

        #Artist href
        all_art_links = [a.get('href') for a in list.find_all('a', attrs={'href': re.compile("^/wiki/")})][1:] 

        #Artist name
        artist_links = ([t.text for t in list.find_all('a')])[1:]

        hot_100_dict ={}
        hot_100_dict['Ranking'] = num
        hot_100_dict['Title'] = all_titles
        hot_100_dict['Song Link'] = all_links
        hot_100_dict['Artist(s)'] = artist_links
        hot_100_dict['Artist Links'] = all_art_links
        csvwriter.writerow(hot_100_dict.values())

with open('Top_100_Hits.csv', 'w', newline='', encoding='utf-8') as file:
    csvwriter = csv.writer(file)
    headers = ['Ranking', 'Title', 'Song Link', 'Artist(s)', 'Artist Links']
    csvwriter.writerow(headers)
    Year_End_Singles(full_list, csvwriter)
    print('Web Scraping Done! List Compiled')