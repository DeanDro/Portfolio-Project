from bs4 import BeautifulSoup
import requests
import random

search_quote = True

while search_quote:

    f = open('./microservices/text_files/quote.txt', 'r')
    content = f.readline()
    f.close()

    if content != '':

        quote_pages = requests.get('https://en.wikiquote.org/wiki/Wikiquote:Quotes_of_the_Year').text
        quotes = BeautifulSoup(quote_pages, 'lxml')

        rant = random.randint(0, 20)

        quotes_segment = quotes.find('div', class_='mw-parser-output')
        quotes_list = quotes_segment.find_all('li')

        quote = quotes_list[rant]

        print(quote)