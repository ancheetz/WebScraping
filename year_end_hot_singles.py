import requests, csv, re, time
import numpy as np
from bs4 import BeautifulSoup as bs

URL = "https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2019"
response = requests.get(URL)

page = (response.text)
soup = bs(page, 'html.parser')


song_num = []
song_title = []
song_link = []
artist = []
artist_link = []
artist_bio = []
artist_song = []

#Collect each row of data for our songs
full_list = soup.find_all('tr')
full_list = full_list[1:101]

#Loop through all data
for list in full_list:
    
    #Song number
    num = list.th.text
    song_num.append(num)

    #Song title
    all_titles = ([t.text for t in list.find_all('a')])
    song = all_titles[0]
    song_title.append(song)

    #Song href
    all_links = [a.get('href') for a in list.find_all('a', attrs={'href': re.compile("^/wiki/")})]
    s_links = all_links[0]
    song_link.append(s_links)

    #Artist href
    all_art_links = [a.get('href') for a in list.find_all('a', attrs={'href': re.compile("^/wiki/")})]
    a_links = all_art_links[1:]
    artist_link.append(a_links)

    #Artist name
    all_artist_links = ([t.text for t in list.find_all('a')])
    art_links = all_artist_links[1:]
    artist.append(art_links)

    ##Bio for Artist

    ##Bio for Song



print(artist_link)
print(song_link)
print(artist)
print(song_title)
print(song_num)

#print(all_links)    
