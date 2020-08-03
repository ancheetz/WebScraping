import requests, csv, time, re
import numpy as np
from bs4 import BeautifulSoup as bs

URL = "https://www.yelp.ca/biz/bar-karaoke-lounge-toronto"
response = requests.get(URL)

page = (response.text)
soup = bs(page, 'html.parser')

#collect number of reviews in total
total_rev = soup.find('div', attrs={'class': 'lemon--div__373c0__1mboc arrange-unit__373c0__o3tjT border-color--default__373c0__3-ifU nowrap__373c0__35McF'}).string.split(' ')[0]
total_rev = int(total_rev)
print(total_rev)

#<p class="lemon--p__373c0__3Qnnj text__373c0__2U54h text-color--mid__373c0__27i5f text-align--left__373c0__1Uy60 text-size--large__373c0__1j9OF">105 reviews</p>

#<div class="lemon--div__373c0__1mboc arrange-unit__373c0__o3tjT border-color--default__373c0__3-ifU nowrap__373c0__35McF"><p class="lemon--p__373c0__3Qnnj text__373c0__2U54h text-color--mid__373c0__27i5f text-align--left__373c0__1Uy60 text-size--large__373c0__1j9OF">105 reviews</p></div>