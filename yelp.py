import requests, re, json, dateutil.parser
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
print(reviewer[0])
print(type(reviewer))
#convert list to json string, formatted with indents
name = (json.dumps(reviewer, indent=4))
#print(name)

#find review
review = [rev.text for rev in soup.find_all('span', lang='en')]
print(review[0])
#convert list to json string, formatted with indents
rest_rev = (json.dumps(review, indent=6))
#print(rest_rev)

#find date of review
date_vis = [d.text for d in soup.find_all('span', class_='text-color--mid__373c0__jCeOG')]
#print(date_vis)
#convert list tp json string,
date_rev = (json.dumps(date_vis, indent=4))
print(date_rev)



