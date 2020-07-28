import csv, re, time, requests
from bs4 import BeautifulSoup as bs

URL = "https://vervewine.com/blogs/roses-we-love"
response = requests.get(URL)

page = response.text
soup = bs(page, 'html.parser')


writeup = soup.find_all('div', attrs={'grid__item small--two-thirds'})
writeup = (writeup[3])

#name = writeup.find('a', attrs={'article__title'}).text
#print(name)

#vintage = writeup.find('a', attrs={'article__title'}).text.split(' ')[-1]
#print(vintage)

#article_date = writeup.find('div', attrs={'article__date'}).text
#print(article_date)

#link_to_article = writeup.find('div', attrs={'article__date'}).find_next('a').get('href')
#print(link_to_article)

description = str(writeup.find('div', attrs={'rte article__excerpt'}).find('span'))
print(description)
