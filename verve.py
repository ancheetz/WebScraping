import csv, re, time, requests
from bs4 import BeautifulSoup as bs

URL = "https://vervewine.com/blogs/roses-we-love"
response = requests.get(URL)

page = response.text
soup = bs(page, 'html.parser')


writeups = soup.find('div', attrs={'grid grid--uniform'})
writeup = soup.find_all('div', attrs={'grid__item small--two-thirds'})
#writeup = writeup[0]

#name = writeup.find('a', attrs={'article__title'}).text
#print(name)

#vintage = writeup.find('a', attrs={'article__title'}).text.split(' ')[-1]
#print(vintage)

#article_date = writeup.find('div', attrs={'article__date'}).text
#print(article_date)

#link_to_article = writeup.find('div', attrs={'article__date'}).find_next('a').get('href')
#print(link_to_article)

#description = writeup.find('span').text
#print(description)

def Wine_Reviews(writeup, csvwriter):
    for w in writeup:
        name = w.find('a', attrs={'article__title'}).text
        vintage = w.find('a', attrs={'article__title'}).text.split(' ')[-1]
        article_date = w.find('div', attrs={'article__date'}).text
        link_to_article = w.find('div', attrs={'article__date'}).find_next('a').get('href')
        description = str(w.find('div', attrs={'rte article__excerpt'}).find('span'))[6:-7]
        wine = {}
        wine['Name'] = name
        wine['Vintage'] = vintage
        wine['Article Date'] = article_date
        wine['Link to Review'] = link_to_article
        wine['Description'] = description
        csvwriter.writerow(wine.values())

with open('Wine Reviews.csv', 'w', encoding='utf-8', newline='') as file:
    csvwriter = csv.writer(file)
    headers = ['Name', 'Vintage', 'Article Date', 'Link to Review', 'Description']
    csvwriter.writerow(headers)
    Wine_Reviews(writeup, csvwriter)
    print('Wine Reviews successfully gathered.')

