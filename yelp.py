import requests, re, json, dateutil.parser
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs

URL = "https://www.yelp.ca/biz/bar-karaoke-lounge-toronto"
response = requests.get(URL)

response.status_code
#print(response.text[:200])

page = response.text
#type(page)

#store the webpage in soup
soup = bs(page, 'lxml')

#find reviewer name
reviewer = [name.text for name in soup.find_all('div', 'a', 'href', class_='user-passport-info')]
#convert list to json string, formatted with indents
name = (json.dumps(reviewer, indent=4))
print(name)

#find review
review = [rev.text for rev in soup.find_all('span', lang='en')]
#convert list to json string, formatted with indents
rest_rev = (json.dumps(review, indent=6))
print(rest_rev)

#find date of review
date_vis = [d.text for d in soup.find_all('span', class_='text-color--mid__373c0__jCeOG')]
#convert list tp json string,
date_rev = (json.dumps(date_vis, indent=4))
print(date_rev)

print(type(date_rev))

yelp_dict = dict(zip(reviewer, review))
print(yelp_dict)

yelp_info = [yelp_dict]
yelp_df = pd.DataFrame(yelp_info)
yelp_df.to_csv('Yelp_Review.csv')