'''
    A Program that takes input from User
    and search it on Flipkart, 
    then show the ITEM, PRICE, and RATINGS
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

search_url = 'https://www.flipkart.com/search?q=__&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
user_input = input("Enter Product Name: ")
if ' ' in user_input:
    user_input = user_input.replace(' ', '%20')
search_url = search_url.replace('__', user_input)

try:
    page = urlopen(search_url)
except:
    print("Error Opening Page!!")

soup = BS(page,'html.parser')

data = soup.findAll('div',{'class':'col col-7-12'})

i=0 #Price Index Extractor
for item in data:

    #Item Name Trimming
    item_name=item.text
    item_name=item_name.split(')')
    print('Name :',item_name[0]+')')

    #Item Price Trimming
    price=soup.findAll('div',{'class':'_1vC4OE _2rQ-NK'})
    item_price=price[i].text
    print('Price :',item_price)
    i=i+1

    #Item Rating Trimming
    item_rating=item_name[1].split(',')[0]
    print('Ratings :',item_rating,'\n')
