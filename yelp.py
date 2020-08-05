import requests, csv, time, dateutil
import mysql
import mysql.connector
from bs4 import BeautifulSoup as bs

URL = "https://www.yelp.ca/biz/bar-karaoke-lounge-toronto"
response = requests.get(URL)

page = (response.text)
soup = bs(page, 'html.parser')

#SQL connection data to connect and save the data
HOST = 'localhost'
USERNAME = 'andrea'
PASSWORD = 'Star1982'
DATABASE = 'andreadb'

#collect number of reviews in total
total_rev = soup.find('div', attrs={'class': 'lemon--div__373c0__1mboc arrange-unit__373c0__o3tjT border-color--default__373c0__3-ifU nowrap__373c0__35McF'}).string.split(' ')[0]
total_rev = int(total_rev)
#print(total_rev)

#collect number of reviews per page 
review_page = soup.find_all('div', attrs={'lemon--div__373c0__1mboc review__373c0__13kpL sidebarActionsHoverTarget__373c0__2kfhE arrange__373c0__2C9bH gutter-2__373c0__1DiLQ grid__373c0__1Pz7f layout-stack-small__373c0__27wVp border-color--default__373c0__3-ifU'})
#print(review_page)

#collect URLs for all pages of reviews; save these to list; 
URLs = []
for all in range(0, total_rev, 20):
    URLs.append(URL+'?start='+str(all))
    print(URLs)

def get_reviews(review_page, r_writer):
    for review in review_page:
        name = review.find('a', attrs={'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE'}).string
        location = review.find('span', attrs={'lemon--span__373c0__3997G text__373c0__2Kxyz text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz text-size--small__373c0__3NVWO'}).string
        date = review.find('span', attrs={'lemon--span__373c0__3997G text__373c0__2Kxyz text-color--mid__373c0__jCeOG text-align--left__373c0__2XGa-'}).text
        rating = int(review.find('img', attrs={'lemon--img__373c0__3GQUb offscreen__373c0__1KofL'}).parent.get('aria-label')[0])
        content = [r.text for r in review.find('p', attrs={'lemon--p__373c0__3Qnnj text__373c0__2Kxyz comment__373c0__3EKjH text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa-'}).children]
        review_dict = {}
        review_dict['name'] = name
        review_dict['location'] = location
        review_dict['date'] = date
        review_dict['rating'] = rating
        review_dict['content'] = content
        r_writer.writerow(review_dict.values())
        #open db connection
        db = mysql.connector.connect(host='localhost', user='andrea', password='Star1982', database='Reviews')
        print(db)
        #prepare a cursor object using cursor() method
        cursor = db.cursor()
        #prepare SQL query to INSERT a record into the database
        sql = "INSERT INTO Reviews(name, location, date, rating, content) VALUES ('{}', '{}', '{}', '{}','{}')".format(name, location, date, rating, content) 
        try: 
            #execute the SQL command
            cursor.execute(sql)
            #commit your changes in the database
            db.commit()
        except:
            #rollback in case there is any error
            db.rollback()
            #disconnect from the server
            db.close()


with open('Yelp_Reviews.csv', 'w', newline='') as f:
    rev_writer = csv.writer(f)
    header_names = ['Name', 'Location', 'Date', 'Rating', 'Content']
    rev_writer.writerow(header_names)
    #must now use collected list of URLs to iterate through all reviews; then calling previous function to scrape one page, write data and compile as CSV
    for index, Url in enumerate(URLs):
        response = requests.get(URL)
        soup = bs(response.text, 'html.parser')
        review_page = soup.find_all('div', attrs={'lemon--div__373c0__1mboc review__373c0__13kpL sidebarActionsHoverTarget__373c0__2kfhE arrange__373c0__2C9bH gutter-2__373c0__1DiLQ grid__373c0__1Pz7f layout-stack-small__373c0__27wVp border-color--default__373c0__3-ifU'})
        #my function
        get_reviews(review_page, rev_writer)
        time.sleep(2)
        print('Completed scraping page'+str(index+1))