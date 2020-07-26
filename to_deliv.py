import requests, re, time, csv
from bs4 import BeautifulSoup as bs
import numpy as np

URL = "https://torontolife.com/food/eight-toronto-restaurants-that-have-morphed-into-markets-selling-groceries-meal-kits-and-food-box-subscriptions/"
response = requests.get(URL)

page = (response.text)
soup = bs(page,'html.parser')

name = []
address = []
link = []
hours_op = []

print(soup)