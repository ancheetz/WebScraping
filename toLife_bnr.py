import requests, csv, re, time
from bs4 import BeautifulSoup as bs

URL = "https://torontolife.com/food/torontos-best-new-restaurants-2020/"
response = requests.get(URL)

page = (response.text)
soup = bs(page, 'html.parser')


#Web Scraping app to collet data for ToLife Best New Restaurants of 2020 & place in CSV file

#One Review
#collect full page of reviews
all_reviews = soup.find_all('article')
all_reviews = all_reviews[2:]
#all_reviews = all_reviews[2]

#collect name of restaurant
#name = str(all_reviews.find('a').parent.get_text('em')).split(',')[0]
#print(name)

#collect address of restaurant
#address = str(all_reviews.find('a').parent.get_text('em')).split(',')[1].encode('ascii', 'ignore')
#print(address)

#collect weblink to restaurant
#link = str(all_reviews.find('a').parent.get_text('em')).split(',')[2]
#print(link)

#collect review of restaurant
#review = [a.text for a in all_reviews.find_all('p')[:-2]]
#print(review)

#resto_dict = {}
#resto_dict['Name'] = name
#resto_dict['Address'] = address
#resto_dict['Link'] = link
#resto_dict['Review'] = review

def One_review(all_reviews, csvwriter):
    for review in all_reviews:
        name = str(review.find('a').parent.get_text('em')).split(',')[0]
        address = str(review.find('a').parent.get_text('em')).split(',')[1]
        link = str(review.find('a').parent.get_text('em')).split(',')[2][3:]
        review = [a.text for a in review.find_all('p')[:-2]]
        resto_dict = {}
        resto_dict['Name'] = name
        resto_dict['Address'] = address
        resto_dict['Link'] = link
        resto_dict['Review'] = review
        csvwriter.writerow(resto_dict.values())

with open('Rest_Review.csv', 'w', newline='', encoding='utf-8') as f:
     Restwriter = csv.writer(f)
     headers = ['Name', 'Address', 'Link', 'Review']
     Restwriter.writerow(headers)
     One_review(all_reviews, Restwriter)
     print('Web Scraping Completed!')
