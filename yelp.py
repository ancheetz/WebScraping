import requests, re
from bs4 import BeautifulSoup as bs

URL = "https://www.yelp.ca/biz/bar-karaoke-lounge-toronto"
response = requests.get(URL)

response.status_code
#print(response.text)

page = response.text
#type(page)

#store the webpage in soup
soup = bs(page)

reviewer = soup.find('a', class_='lemon')['href']
reviewer

