import requests, csv, re, time
from bs4 import BeautifulSoup as bs

URL = "https://torontolife.com/food/bars-and-clubs/30-best-toronto-bars/"
response = requests.get(URL)

page = (response.text)
soup = bs(page, 'html.parser')


#Web Scraping app to collet data for ToLife Best New Restaurants of 2020 & place in CSV file

#One Review
#collect full page of reviews
all_reviews = soup.find_all('article')
all_reviews = all_reviews[2:]
#print(all_reviews)

#collect name of restaurant
#name = soup.find('div', attrs={'package-list-wrap js-package-list-wrap'}).find_all('a')
#print(name)

#collect address of restaurant
#address = str(all_reviews.find('a').parent.get_text('em')).split(',')[0]
#print(address)

#collect weblink to restaurant
#link = str(all_reviews.find('a').get_text('em'))
#print(link)

#collect review of restaurant
#review = [a.text for a in all_reviews.find_all('p')[:-2]]
#print(review)

#resto_dict = {}
#resto_dict['Name'] = name
#resto_dict['Address'] = address
#resto_dict['Link'] = link
#resto_dict['Review'] = review


        
def Top_Reviews(all_reviews, csvwriter):
    for review in all_reviews:
        address = str(review.find('a').parent.get_text('em')).split(',')[0]
        link = str(review.find('a').get_text('em'))
        review = [a.text for a in review.find_all('p')[:-2]]
        resto_dict = {}
        #resto_dict['Name'] = name
        resto_dict['Address'] = address
        resto_dict['Link'] = link
        resto_dict['Review'] = review
        csvwriter.writerow(resto_dict.values())

with open('Bar_Review.csv', 'w', newline='', encoding='utf-8') as f:
    bar_writer = csv.writer(f)
    headers = ['Address', 'Link', 'Review']
    bar_writer.writerow(headers)
    Top_Reviews(all_reviews, bar_writer)
    print('Web Scraping Completed!')

