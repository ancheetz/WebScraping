from bs4 import BeautifulSoup 
import requests, csv, json

source = requests.get('https://www.crummy.com/software/BeautifulSoup/bs4/doc/')
page = source.text
soup = BeautifulSoup(page, 'lxml')

#print(source.status_code)
#print(source.text)

#body= soup.find_all('p')
#for p in body:
#    print(p.text)

par1 = [p.text for p in soup.find_all('p')]
print(par1[0])
