import requests, csv, time, re
import numpy as np
from bs4 import BeautifulSoup as bs

URL = "https://www.yelp.com/biz/the-four-horsemen-brooklyn"
response = requests.get(URL)

page = (response.text)
soup = bs(page, 'html.parser')

#Find all reviews in site
reviews = soup.find_all('div', attrs={'lemon--div__373c0__1mboc review__373c0__13kpL sidebarActionsHoverTarget__373c0__2kfhE arrange__373c0__2C9bH gutter-2__373c0__1DiLQ grid__373c0__1Pz7f layout-stack-small__373c0__27wVp border-color--default__373c0__3-ifU'})
num_reviews = len(reviews)
print(num_reviews)
reviews = reviews

#Number of reviews
total_reviews = soup.find('div', attrs={'lemon--div__373c0__1mboc arrange-unit__373c0__o3tjT border-color--default__373c0__3-ifU nowrap__373c0__35McF'}).string.split(' ')[0]
#total_reviews = int(total_reviews)
print(total_reviews)

#All URLs to scrape
urls = []
for n in range(0, total_reviews, 20):
    urls.append(URL+'?start='+str(n))

