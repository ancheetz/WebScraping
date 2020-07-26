import requests, csv, time, re
import numpy as np
from bs4 import BeautifulSoup as bs

URL = "https://www.yelp.com/biz/the-four-horsemen-brooklyn"
response = requests.get(URL)

page = (response.text)
soup = bs(page, 'html.parser')

name = []
location = []
rating = []
num_visits = []
review = []

reviews = soup.find_all('div', attrs={'lemon--div__373c0__1mboc review__373c0__13kpL sidebarActionsHoverTarget__373c0__2kfhE arrange__373c0__2C9bH gutter-2__373c0__1DiLQ grid__373c0__1Pz7f layout-stack-small__373c0__27wVp border-color--default__373c0__3-ifU'})
print(reviews[2])