import requests, re, dateutil
from bs4 import BeautifulSoup as bs

URL = "https://www.yelp.ca/biz/bar-karaoke-lounge-toronto"
response = requests.get(URL)

page = (response.text)
soup = bs(page, 'html.parser')


#collect number of reviews
total_rev = [t.text for t in soup.find_all('p', attrs={'class': 'lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--mid__373c0__jCeOG text-align--left__373c0__2XGa- text-size--large__373c0__3t60B'})][0]
total_rev = int(total_rev.split(' ')[0])
print(total_rev)

#collect entire page of reviews and full resource
review_page = soup.find_all('div', attrs={'lemon--div__373c0__1mboc review__373c0__13kpL sidebarActionsHoverTarget__373c0__2kfhE arrange__373c0__2C9bH gutter-2__373c0__1DiLQ grid__373c0__1Pz7f layout-stack-small__373c0__27wVp border-color--default__373c0__3-ifU'})
# number of reviews per page
revs_page = (len(review_page))
print(type(revs_page))

#collect number of reviews per page
review_page = soup.find_all('div', attrs={'lemon--div__373c0__1mboc review__373c0__13kpL sidebarActionsHoverTarget__373c0__2kfhE arrange__373c0__2C9bH gutter-2__373c0__1DiLQ grid__373c0__1Pz7f layout-stack-small__373c0__27wVp border-color--default__373c0__3-ifU'})
print(len(review_page))

#this will give you details for specified entry
review_page = review_page[1]

#collect the name of the reviewer
name = review_page.find('a', attrs={'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE'}).string
print(name)

#collect location of reviewer
location = review_page.find('span', attrs={'lemon--span__373c0__3997G text__373c0__2Kxyz text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz text-size--small__373c0__3NVWO'}).string
print(location)

#collect the date reviewed
date = review_page.find('span', attrs={'lemon--span__373c0__3997G text__373c0__2Kxyz text-color--mid__373c0__jCeOG text-align--left__373c0__2XGa-'}).text
print(date)

#collect rating
rating = int(review_page.find('img', attrs={'lemon--img__373c0__3GQUb offscreen__373c0__1KofL'}).parent.get('aria-label')[0])
print(rating)

#collect review
review = [r.text for r in review_page.find('p', attrs={'lemon--p__373c0__3Qnnj text__373c0__2Kxyz comment__373c0__3EKjH text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa-'}).children]
print(review)

review_dict = {}
review_dict['name'] = review_page.find('a', attrs={'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE'}).string
review_dict['location'] = review_page.find('span', attrs={'lemon--span__373c0__3997G text__373c0__2Kxyz text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz text-size--small__373c0__3NVWO'}).string
review_dict['date'] = review_page.find('span', attrs={'lemon--span__373c0__3997G text__373c0__2Kxyz text-color--mid__373c0__jCeOG text-align--left__373c0__2XGa-'}).text
review_dict['rating'] = int(review_page.find('img', attrs={'lemon--img__373c0__3GQUb offscreen__373c0__1KofL'}).parent.get('aria-label')[0])
review_dict['review'] = [r.text for r in review_page.find('p', attrs={'lemon--p__373c0__3Qnnj text__373c0__2Kxyz comment__373c0__3EKjH text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa-'}).children]

print(review_dict)