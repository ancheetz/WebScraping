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
total_reviews = int(total_reviews)
print(total_reviews)

#All URLs to scrape
urls = []
for n in range(0, total_reviews, 20):
    urls.append(URL+'?start='+str(n))

#Reviewer name
#name = reviews.find('a', attrs={'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE'}).text
#print(name)

#Reviewer location
#location = reviews.find('span', attrs={'lemon--span__373c0__3997G text__373c0__2Kxyz text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz text-size--small__373c0__3NVWO'}).text
#print(location)

#Review Date
#date = reviews.find('span', attrs={'lemon--span__373c0__3997G text__373c0__2Kxyz text-color--mid__373c0__jCeOG text-align--left__373c0__2XGa-'}).string
#print(date)

#Review Star Rating
#rating = reviews.find('img', attrs={'lemon--img__373c0__3GQUb offscreen__373c0__1KofL'}).parent.get('aria-label')[0]
#print(rating)

#Review
#review = reviews.find('span', attrs={'lemon--span__373c0__3997G raw__373c0__3rKqk'}).text
#print(review)

def Create_Review(reviews, csvwriter):
    for one in reviews:
        name = one.find('a', attrs={'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE'}).text
        location = one.find('span', attrs={'lemon--span__373c0__3997G text__373c0__2Kxyz text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz text-size--small__373c0__3NVWO'}).text
        date = one.find('span', attrs={'lemon--span__373c0__3997G text__373c0__2Kxyz text-color--mid__373c0__jCeOG text-align--left__373c0__2XGa-'}).text
        rating = one.find('img', attrs={'lemon--img__373c0__3GQUb offscreen__373c0__1KofL'}).parent.get('aria-label')[0]
        review = one.find('span', attrs={'lemon--span__373c0__3997G raw__373c0__3rKqk'}).text
        rev_dict = {}
        rev_dict['Name'] = name
        rev_dict['Location'] = location
        rev_dict['Date'] = date
        rev_dict['Rating'] = rating
        rev_dict['Review'] = review
        csvwriter.writerow(rev_dict.values())

with open('Reviews.csv', 'w', newline='', encoding='utf-8') as file:
    csvwriter = csv.writer(file)
    headers = ['Name', 'Location', 'Date', 'Rating', 'Review']
    csvwriter.writerow(headers)
    for index, url in enumerate(urls):
        response = requests.get(URL)
        soup = bs(response.text, 'html.parser')
        Create_Review(reviews, csvwriter)
        time.sleep(2)
        print('Completed Reviews. Page '+str(index))
